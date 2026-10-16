from instaloader import Profile
import instaloader

loader = instaloader.instaloader()
username = input("enter username: ")

profile = Profile.from_username(
    loader.context, username
)
new_followers = []

for follower in profile.get_followees():
    new_followers.append(follower.username)

print("new followers:" new_followers)