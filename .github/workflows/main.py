import os
import requests
from redmail import EmailSender
from dotenv import load_dotenv
from dotenv import find_dotenv

# Define your GitHub username
username = "sumonta056"
useremail = "sumontasaha80@gmail.com"

# API URL to fetch user data
api_url = f"https://api.github.com/users/{username}"

# Function to get the current follower count from the GitHub API
def get_follower_count():
    user_data = requests.get(api_url).json()
    return user_data["followers"]

# Function to read the follower count from a text file
def read_follower_count_from_file():
    try:
        with open("follower_count.txt", "r") as file:
            return int(file.read().strip())
    except FileNotFoundError:
        return 0

# Function to update the follower count in the text file
def update_follower_count_in_file(count):
    with open("follower_count.txt", "w") as file:
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
        sender="gitfollowernotifierbysumonta56@gmail.com",
        receivers=useremail,
        text=body,
    )


# Get the current and saved follower counts
current_followers = get_follower_count()
saved_followers = read_follower_count_from_file()

# Compare follower counts and send email if current count is greater
if current_followers > saved_followers:
    subject = "🎉 Congratulations! You Have a New Follower on GitHub! 🚀"
    body = f""" Hey {username},

    Exciting news! You've just earned yourself a new follower on GitHub. 🎉

    It's awesome to see your community growing and your work getting recognized. Keep up the fantastic contributions!

    Stay inspired and keep coding!

    Total Followers: {current_followers}"""

    send_email(body, subject)

    # Update follower count in the file
    update_follower_count_in_file(current_followers)
else:
    subject = "🚀 Your GitHub Follower Count Update 🌟"
    body = f""" Hey {username},
        Total Followers: {current_followers}"""

    send_email(body, subject)
