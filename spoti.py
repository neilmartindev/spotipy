import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

# Get the username from terminal
username = sys.argv[1]

# Erase cache and prompt
try:
    token = util.prompt_for_user_token(username)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username)

# Create object
spotifyObject = spotipy.Spotify(auth=token)

user = spotifyObject.current_user()

print(json.dumps(user, sort_keys=True, indent=4))

dispayName = user['display_name']
followers = user['followers'] ['total']

while True:

    print()
    print(">>>> Welcome to Spotipy " + displayName + "!")
    print(">>>> You have " + str(followers) + "followers.")
    print()
    print("0 - Search for an artist")
    print("1 - Exit")
    choice = input(" Your choice: ")

    # Search for the
    if choice == 0:
        print("0")
    
    if choice == 1:
        break



# print(json.dumps(VARIABLE, sort_keys=True, indent=4))

# git test
