# SORSE retweet bot

This is a very simple Python Twitter bot that likes and retweets all tweets made by Twitter user `@Int_SORSE`.

## Requirements

- Python 3
- The following environment variables must be set and be readable by Python's `os.environ`:
  - `API_KEY`: The Twitter API Key
  - `API_KEY_SECRET`: The Twitter API Key secret
  - `ACCESS_TOKEN`: The Twitter Access Token
  - `ACCESS_TOKEN_SECRET`: The Twitter Access Token 
- A file named `last_seen.txt` must be present in this directory, which contains nothing but the ID of the most recent tweet you do **not** want to retweet. All tweets newer than the tweet with this ID will be retweeted and liked! To retrieve the tweet ID of the most recent tweet that should be ignored, simply open it on twitter.com, and copy the long integer following `https://twitter.com/Int_SORSE/status/`, e.g. `https://twitter.com/Int_SORSE/status/`**`1320664355046887428`**.
- You need to register a Twitter developer account at <https://developer.twitter.com>, and create and save the API key and secret. You also need to create a Twitter app with read and write permissions, and mint an access token and secret.

## Run the bot locally

To run the bot locally, do the following (example run on Ubuntu 20.04):

```bash
# Change into the directory that contains the root of this repository
cd sorse-retweet-bot
# Create a new virtual environment
python3 -m venv venv
# Start the new virtual environment
source venv/bin/activate
# Upgrade pip
pip install --upgrade pip
# Install dependencies
pip install -r requirements.txt
# Set the required variables (see above)
export API_KEY=... # Use your own API key, etc.
export API_KEY_SECRET=...
export ACCESS_TOKEN=...
export ACCESS_TOKEN_SECRET=...
# Create the file containing the ID of the tweet that the bot has "last seen"
echo "1234567890" > last_seen.txt # Use a real tweet ID
# Run the bot, wait for Int_SORSE to tweet something and watch it being retweeted and liked by your account
python bot.py
```

## Deploy to Heroku

1. Get an account on <https://heroku.com>.
2. Install the [`heroku` command line tool](https://devcenter.heroku.com/articles/heroku-cli#download-and-install).
3. Login to Heroku via the command line tool with `heroku login`.
4. In the root of the repository, run `heroku create` which will set up a Heroku app and create a `heroku` remote for the repository.
5. Set the environment variables for the Heroku app:
   1. `heroku config:set API_KEY=...`
   2. `heroku config:set API_KEY_SECRET=...`
   3. `heroku config:set ACCESS_TOKEN=...`
   4. `heroku config:set ACCESS_TOKEN_SECRET=...`
6. Deploy the app by running `git push heroku main`.
7. Start the worker on Heroku by running `heroku ps:scale worker=1`.