import instaloader
import pyshorteners
import sys
import signal
from termcolor import colored
import os

# Clear the screen
if os.name == 'posix':
    os.system('clear')
else:
    os.system('cls')

 
# banner
print(colored("""

 _           _        _        __       
(_)_ __  ___| |_ __ _(_)_ __  / _| ___  
| | '_ \/ __| __/ _` | | '_ \| |_ / _ \ 
| | | | \__ \ || (_| | | | | |  _| (_) |
|_|_| |_|___/\__\__,_|_|_| |_|_|  \___/ 
                                        
""", "red"))
print(colored("   <---(( Coded by cyberxaman ))--> \n", "yellow"))
print(colored("-----------------------------------------", "cyan"))
print(colored("-----------------------------------------", "cyan"))

def signal_handler(sig, frame):
    print(colored("\nProgram interrupted. Goodbye! 👋", "red"))
    sys.exit(0)

# Register signal handler to handle CTRL+C interrupts
signal.signal(signal.SIGINT, signal_handler)

# Create an instance of the Instaloader class
L = instaloader.Instaloader()

# Get the username from the user
username = input(colored("\nEnter an Instagram username: ", "green"))

try:
    # Get a Profile instance corresponding to the username
    profile = instaloader.Profile.from_username(L.context, username)

    # Print some basic profile information
    print(colored("-----------", "green"))
    print("Username:", colored(profile.username, "blue"))
    print(colored("-----------", "green"))
    print("Full Name:", colored(profile.full_name, "blue"))
    print(colored("-----------", "green"))
    print("Bio:", colored(profile.biography, "blue"))
    print(colored("-----------", "green"))
    print("Number of Posts:", colored(profile.mediacount, "blue"))
    print(colored("-----------", "green"))
    print("Number of Followers:", colored(profile.followers, "blue"))
    print(colored("-----------", "green"))
    print("Number of Followees:", colored(profile.followees, "blue"))
    print(colored("-----------", "green"))
    print("\nPrivate Account:", colored("Yes" if profile.is_private else "No", "blue"))
    print(colored("-----------", "green"))

    # Shorten the profile picture URL using pyshorteners
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(profile.profile_pic_url)
    print("Profile Picture URL:", colored(short_url, "blue"))
    print(colored("-----------", "green"))

    # Get the short profile URL link
    short_url = f"https://www.instagram.com/{profile.username}/"
    print("Profile URL:", colored(short_url, "blue"))
    print(colored("-----------", "green"))

    # Print the user's posts and the number of likes and comments for each post
    posts = profile.get_posts()
    num_posts = profile.mediacount
    print(colored("\nPosts:", "cyan"))
    print(colored("-----------", "cyan"))
    print(f"Total number of posts: {colored(num_posts, 'blue')}")
    print(colored("-----------", "cyan"))
    for i, post in enumerate(posts):
        print(f"Post {i+1} has {colored(post.likes, 'blue')} likes and {colored(post.comments, 'blue')} comments")
        print("Post URL:", colored(s.tinyurl.short(post.url), "blue"))
        print("Location:", colored(post.location, "blue"))
        if i != num_posts - 1:
            print(colored("-----------", "cyan"))
    print(colored("\n-----------😀", "yellow"))

except instaloader.exceptions.ProfileNotExistsException:
    print(colored("The username entered does not exist. Please try again.", "red"))
    sys.exit(0)
except Exception as e:
    print(colored("An error occurred. Please try again.", "red"))
    sys.exit(0)
