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

def send_email(body,subject,name,follow):
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
        html= body,
        body_params={
        'username': name,
        'follwer': follow
        }
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
    
    html1 = """
   <!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>New Follower on GitHub</title>
    <style>
      body {
        font-family: Arial, sans-serif;
        background-color: #f4f4f4;
        padding: 20px;
      }

      h1 {
        color: #333;
      }

      p {
        color: #666;
        font-size: 16px;
        line-height: 1.6;
      }

      .container {
        max-width: 600px;
        margin: 0 auto;
        background-color: #fff;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
      }
      .card {
        max-width: 320px;
        border-width: 1px;
        border-color: rgba(219, 234, 254, 1);
        border-radius: 1rem;
        background-color: rgba(255, 255, 255, 1);
        padding: 1rem;
      }

      .header {
        display: flex;
        align-items: center;
        grid-gap: 1rem;
        gap: 1rem;
      }

      .icon {
        flex-shrink: 0;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 9999px;
        background-color: rgba(96, 165, 250, 1);
        padding: 0.5rem;
        color: rgba(255, 255, 255, 1);
      }

      .icon svg {
        height: 1rem;
        width: 1rem;
      }

      .alert {
        font-weight: 600;
        color: rgba(107, 114, 128, 1);
      }

      .message {
        margin-top: 1rem;
        color: rgba(107, 114, 128, 1);
      }

      .actions {
        margin-top: 1.5rem;
      }

      .actions a {
        text-decoration: none;
      }

      .mark-as-read,
      .read {
        display: inline-block;
        border-radius: 0.5rem;
        width: 100%;
        padding: 0.75rem 1.25rem;
        text-align: center;
        font-size: 0.875rem;
        line-height: 1.25rem;
        font-weight: 600;
      }

      .read {
        background-color: rgba(59, 130, 246, 1);
        color: rgba(255, 255, 255, 1);
      }

      .mark-as-read {
        margin-top: 0.5rem;
        background-color: rgba(249, 250, 251, 1);
        color: rgba(107, 114, 128, 1);
        transition: all 0.15s ease;
      }

      .mark-as-read:hover {
        background-color: rgb(230, 231, 233);
      }
    </style>
  </head>
  <body>
    <div class="container">
      <h1>Hi {{username}},</h1>

      <p>
        Exciting news! You've just earned yourself a new follower on GitHub. 🎉
      </p>

      <p>
        It's awesome to see your community growing and your work getting
        recognized. Keep up the fantastic contributions!
      </p>

      <p>Stay inspired and keep coding!</p>

      <p>Total Followers: {{current_followers}} </p>
    </div>
    <div class="card">
      <div class="header">
        <span class="icon">
          <svg
            fill="currentColor"
            viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              clip-rule="evenodd"
              d="M18 3a1 1 0 00-1.447-.894L8.763 6H5a3 3 0 000 6h.28l1.771 5.316A1 1 0 008 18h1a1 1 0 001-1v-4.382l6.553 3.276A1 1 0 0018 15V3z"
              fill-rule="evenodd"
            ></path>
          </svg>
        </span>
        <p class="alert">New message!</p>
      </div>

      <p class="message">
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Ipsam ea quo
        unde vel adipisci blanditiis voluptates eum. Nam, cum minima?
      </p>

      <div class="actions">
        <a class="read" href=""> Take a Look </a>

        <a class="mark-as-read" href=""> Mark as Read </a>
      </div>
    </div>
  </body>
</html>

    """


    send_email(html1, subject,username,current_followers)

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