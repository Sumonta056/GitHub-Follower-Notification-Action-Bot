import os
import requests
from redmail import EmailSender

# Define your variables
username = "sumonta056"
useremail = "sumontasaha80@gmail.com"
botmail = "gitfollowernotifierbysumonta56@gmail.com"

# API URL to fetch user data
api_url = f"https://api.github.com/users/{username}"
link = "https://github.com/{username}"
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
        password=password,
    )

    email.send(
        subject=subject,
        sender=botmail,
        receivers=useremail,
        html= body,
        body_params={
        'username': name,
        'current_followers': follow,
        'link': link
        }
    )


# Get the current and saved follower counts
current_followers = get_follower_count()
saved_followers = read_follower_count_from_file()

# Compare follower counts and send email if current count is greater
if current_followers > saved_followers:
    subject = "🎉 Congratulations! You Have a New Follower on GitHub! 🚀"
    link = "https://github.com/{username}?tab=followers"
    html = """
     <div style="max-width: 600px; margin: 0 auto; background-color: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);">
        <h1 style="color: #333;">Hi {{username}} 👋👋,</h1>
    
        <p style="color: #666; font-size: 16px; line-height: 1.6;">
        Exciting news! You've just earned yourself a new follower on GitHub. 🎉
        </p>
    
        <p style="color: #666; font-size: 16px; line-height: 1.6;">
        It's awesome to see your community growing and your work getting recognized. Keep up the fantastic contributions!
        </p>
    
        <p style="color: #666; font-size: 16px; line-height: 1.6;">Stay inspired and keep coding!</p>
    
        <p style="color: #662; font-size: 20px; line-height: 1.6;">Total Followers: {{current_followers}}</p>
        
        <a href={{link}} style="text-decoration: none;">
        <button style="display: flex; justify-content: center; align-items: center; padding: 2px 70px; gap: 15px; background-color: #181717; outline: 3px #181717 solid; outline-offset: -3px; border-radius: 5px; border: none; cursor: pointer; transition: 400ms;">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style="transition: 400ms;">
          <path d="M12 0.296997C5.37 0.296997 0 5.67 0 12.297C0 17.6 3.438 22.097 8.205 23.682C8.805 23.795 9.025 23.424 9.025 23.105C9.025 22.82 9.015 22.065 9.01 21.065C5.672 21.789 4.968 19.455 4.968 19.455C4.422 18.07 3.633 17.7 3.633 17.7C2.546 16.956 3.717 16.971 3.717 16.971C4.922 17.055 5.555 18.207 5.555 18.207C6.625 20.042 8.364 19.512 9.05 19.205C9.158 18.429 9.467 17.9 9.81 17.6C7.145 17.3 4.344 16.268 4.344 11.67C4.344 10.36 4.809 9.29 5.579 8.45C5.444 8.147 5.039 6.927 5.684 5.274C5.684 5.274 6.689 4.952 8.984 6.504C9.944 6.237 10.964 6.105 11.984 6.099C13.004 6.105 14.024 6.237 14.984 6.504C17.264 4.952 18.269 5.274 18.269 5.274C18.914 6.927 18.509 8.147 18.389 8.45C19.154 9.29 19.619 10.36 19.619 11.67C19.619 16.28 16.814 17.295 14.144 17.59C14.564 17.95 14.954 18.686 14.954 19.81C14.954 21.416 14.939 22.706 14.939 23.096C14.939 23.411 15.149 23.786 15.764 23.666C20.565 22.092 24 17.592 24 12.297C24 5.67 18.627 0.296997 12 0.296997Z" fill="white"></path>
        </svg>
        <p style="color: white; font-weight: 700; font-size: 1.2em; transition: 400ms;">Check Followers</p>
        </button>
        </a>
        </div>
    """

    send_email(html, subject,username,current_followers)

    # Update follower count in the file
    update_follower_count_in_file(current_followers)

elif current_followers < saved_followers:
    subject = "Oh No! You've Lost a Follower on GitHub 😔"
    
    
    html = """
     <div style="max-width: 600px; margin: 0 auto; background-color: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);">
        <h1 style="color: #333;">Hi {{username}} 👋👋,</h1>
    
        <p style="color: #666; font-size: 16px; line-height: 1.6;">
        We wanted to let you know that you've lost a follower on GitHub. 🥺🥺
        </p>
    
        <p style="color: #666; font-size: 16px; line-height: 1.6;">
        While it can be disappointing, remember that growth isn't always linear, and people's interests may shift over time 😟😟
        </p>
        
        <p style="color: #666; font-size: 16px; line-height: 1.6;">
       Keep focusing on your projects and contributions. Your work speaks for itself, and your community appreciates your efforts.
        </p>
    
        <p style="color: #666; font-size: 16px; line-height: 1.6;">Stay inspired and keep coding!</p>
    
        <p style="color: #662; font-size: 20px; line-height: 1.6;">Total Followers: {{current_followers}}</p>
        
        <a href={{link}} style="text-decoration: none;">
        <button style="display: flex; justify-content: center; align-items: center; padding: 2px 70px; gap: 15px; background-color: #181717; outline: 3px #181717 solid; outline-offset: -3px; border-radius: 5px; border: none; cursor: pointer; transition: 400ms;">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style="transition: 400ms;">
          <path d="M12 0.296997C5.37 0.296997 0 5.67 0 12.297C0 17.6 3.438 22.097 8.205 23.682C8.805 23.795 9.025 23.424 9.025 23.105C9.025 22.82 9.015 22.065 9.01 21.065C5.672 21.789 4.968 19.455 4.968 19.455C4.422 18.07 3.633 17.7 3.633 17.7C2.546 16.956 3.717 16.971 3.717 16.971C4.922 17.055 5.555 18.207 5.555 18.207C6.625 20.042 8.364 19.512 9.05 19.205C9.158 18.429 9.467 17.9 9.81 17.6C7.145 17.3 4.344 16.268 4.344 11.67C4.344 10.36 4.809 9.29 5.579 8.45C5.444 8.147 5.039 6.927 5.684 5.274C5.684 5.274 6.689 4.952 8.984 6.504C9.944 6.237 10.964 6.105 11.984 6.099C13.004 6.105 14.024 6.237 14.984 6.504C17.264 4.952 18.269 5.274 18.269 5.274C18.914 6.927 18.509 8.147 18.389 8.45C19.154 9.29 19.619 10.36 19.619 11.67C19.619 16.28 16.814 17.295 14.144 17.59C14.564 17.95 14.954 18.686 14.954 19.81C14.954 21.416 14.939 22.706 14.939 23.096C14.939 23.411 15.149 23.786 15.764 23.666C20.565 22.092 24 17.592 24 12.297C24 5.67 18.627 0.296997 12 0.296997Z" fill="white"></path>
        </svg>
        <p style="color: white; font-weight: 700; font-size: 1.2em; transition: 400ms;">Check Followers</p>
        </button>
        </a>
        </div>
    """

    send_email(html, subject,username,current_followers)

    # Update follower count in the file
    update_follower_count_in_file(current_followers)
    
else:
    subject = "🚀 Your GitHub Follower Count Update 🌟"
    link = "https://github.com/{username}?tab=followers"
    html = """
     <div style="max-width: 600px; margin: 0 auto; background-color: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);">
        <h1 style="color: #333;">Hi {{username}} 👋👋,</h1>
        
        <p style="color: #666; font-size: 16px; line-height: 1.6;">Stay inspired and keep coding!</p>
    
        <p style="color: #662; font-size: 20px; line-height: 1.6;">Total Followers: {{current_followers}}</p>
        
        <a href={{link}} style="text-decoration: none;">
        <button style="display: flex; justify-content: center; align-items: center; padding: 2px 70px; gap: 15px; background-color: #181717; outline: 3px #181717 solid; outline-offset: -3px; border-radius: 5px; border: none; cursor: pointer; transition: 400ms;">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style="transition: 400ms;">
          <path d="M12 0.296997C5.37 0.296997 0 5.67 0 12.297C0 17.6 3.438 22.097 8.205 23.682C8.805 23.795 9.025 23.424 9.025 23.105C9.025 22.82 9.015 22.065 9.01 21.065C5.672 21.789 4.968 19.455 4.968 19.455C4.422 18.07 3.633 17.7 3.633 17.7C2.546 16.956 3.717 16.971 3.717 16.971C4.922 17.055 5.555 18.207 5.555 18.207C6.625 20.042 8.364 19.512 9.05 19.205C9.158 18.429 9.467 17.9 9.81 17.6C7.145 17.3 4.344 16.268 4.344 11.67C4.344 10.36 4.809 9.29 5.579 8.45C5.444 8.147 5.039 6.927 5.684 5.274C5.684 5.274 6.689 4.952 8.984 6.504C9.944 6.237 10.964 6.105 11.984 6.099C13.004 6.105 14.024 6.237 14.984 6.504C17.264 4.952 18.269 5.274 18.269 5.274C18.914 6.927 18.509 8.147 18.389 8.45C19.154 9.29 19.619 10.36 19.619 11.67C19.619 16.28 16.814 17.295 14.144 17.59C14.564 17.95 14.954 18.686 14.954 19.81C14.954 21.416 14.939 22.706 14.939 23.096C14.939 23.411 15.149 23.786 15.764 23.666C20.565 22.092 24 17.592 24 12.297C24 5.67 18.627 0.296997 12 0.296997Z" fill="white"></path>
        </svg>
        <p style="color: white; font-weight: 700; font-size: 1.2em; transition: 400ms;">Check Followers</p>
        </button>
        </a>
        </div>
    """

    send_email(html, subject,username,current_followers)