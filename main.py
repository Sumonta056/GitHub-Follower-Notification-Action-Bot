import os
import requests
from redmail import EmailSender

# Define your variables
username = "sumonta056"
useremail = "sumontasaha80@gmail.com"
botmail = "gitfollowernotifierbysumonta56@gmail.com"

# API URL to fetch user data
api_url = f"https://api.github.com/users/{username}"

# Function to get the current follower count from the GitHub API
def get_follower_count():
    user_data = requests.get(api_url).json()
    return user_data["followers"]

# Function to read the follower count from a text file
def read_follower_count_from_file():
    try:
        with open(".github/workflows/follower_count.txt", "r") as file:
            return int(file.read().strip())
    except FileNotFoundError:
        return 0

# Function to update the follower count in the text file
def update_follower_count_in_file(count):
    with open(".github/workflows/follower_count.txt", "w") as file:
        file.write(str(count))

def send_email(body,subject):
    # Send email notification
    username = os.environ.get("USEREMAIL")
    password = os.environ.get("PASSWORD")

    email = EmailSender(
        host='smtp.gmail.com',
        port='587',
        username=username,
        password=password
    )

    email.send(
        subject=subject,
        sender=botmail,
        receivers=useremail,
        text=body,
        html= body
    )


# Get the current and saved follower counts
current_followers = get_follower_count()
saved_followers = read_follower_count_from_file()

# Compare follower counts and send email if current count is greater
if current_followers > saved_followers:
    subject = "🎉 Congratulations! You Have a New Follower on GitHub! 🚀"
    
    html = """
    <div style="max-width: 600px; margin: 0 auto; background-color: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);">
    <h1 style="color: #333;">Hi {username},</h1>

    <p style="color: #666; font-size: 16px; line-height: 1.6;">
    Exciting news! You've just earned yourself a new follower on GitHub. 🎉
    </p>

    <p style="color: #666; font-size: 16px; line-height: 1.6;">
    It's awesome to see your community growing and your work getting recognized. Keep up the fantastic contributions!
    </p>

    <p style="color: #666; font-size: 16px; line-height: 1.6;">Stay inspired and keep coding!</p>

    <p style="color: #662; font-size: 20px; line-height: 1.6;">Total Followers: {current_followers}</p>
    </div>
    """


    send_email(html, subject)

    # Update follower count in the file
    update_follower_count_in_file(current_followers)

elif current_followers < saved_followers:
    subject = "Oh No! You've Lost a Follower on GitHub 😔"
    body = f"""
Hey {username},

We wanted to let you know that you've lost a follower on GitHub. While it can be disappointing, remember that growth isn't always linear, and people's interests may shift over time.

Keep focusing on your projects and contributions. Your work speaks for itself, and your community appreciates your efforts.

Stay positive and keep coding!

Total Followers: {current_followers}"""



    send_email(body, subject)

    # Update follower count in the file
    update_follower_count_in_file(current_followers)
    
else:
    subject = "🚀 Your GitHub Follower Count Update 🌟"
    body = f""" 
Hey {username},
    Total Followers: {current_followers}"""

    send_email(body, subject)