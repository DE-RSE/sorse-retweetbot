# SPDX-License-Identifier: MIT

from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
import time
import os

# Set constants
LAST_SEEN_FILE_PATH = "./last_seen.txt"
RETWEET_USER = "Int_SORSE"

# The following four variables must be available as environment variables
# Our consumer key
api_key = os.environ["API_KEY"]
# Our consumer secret
api_secret = os.environ["API_KEY_SECRET"]
# Our access token
access_token = os.environ["ACCESS_TOKEN"]
# Our access token secret
access_secret = os.environ["ACCESS_TOKEN_SECRET"]

# Authenticate using OAuth 1a authentication.
# See http://docs.tweepy.org/en/v3.9.0/auth_tutorial.html#oauth-1a-authentication.
auth = OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret)

# Get the API object using the defined authentication
api = API(auth)

def read_last_seen():
    """Reads the last seen tweet ID.

    Reads the ID of the most recently retweeted tweet from a file 
    in the path specified by the LAST_SEEN_FILE_PATH constant, and 
    returns it as an integer.
    """
    # Read file and
    with open(LAST_SEEN_FILE_PATH, "r") as file:
        last_seen_id = int(file.read().strip())
        return last_seen_id


def write_last_seen(last_seen_id):
    """Write the last seen tweet ID.

    Writes the string of the ID of the most recently retweeted tweet
    to a file in the path specified by the LAST_SEEN_FILE_PATH constant.
    """
    with open(LAST_SEEN_FILE_PATH, "w") as file:
        file.write(str(last_seen_id))
    return


def reply():
    """Replies to tweets by RETWEET_USER.

    Reads the tweets made by the user with the name specified by the
    RETWEET_USER constant starting from the first tweet after the
    most recently retweeted one.
    """
    # Get all (available) status texts by Int_SORSE after last seen tweet id
    id = read_last_seen()
    new_tweets = []
    new_statuses = Cursor(api.user_timeline, id=RETWEET_USER, since_id=id).items()

    # Add all new statuses since the last seen to list
    for status in new_statuses:
        new_tweets.append(status.id)

    # If there were any new tweets, retweet them
    if len(new_tweets) > 0:
        # Write last status
        write_last_seen(new_tweets[0])

        for id in reversed(new_tweets):
            # Favourite this tweet
            api.create_favorite(id)
            # Retweet
            api.retweet(id)


def main():
    """Runs the bot.

    Calls reply() every 60 seconds forever.
    """
    while True:
        reply()
        time.sleep(60)


if __name__ == "__main__":
    main()