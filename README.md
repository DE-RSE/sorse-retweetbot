# SORSE retweet bot

This is a very simple Python Twitter bot that likes and retweets all tweets made by Twitter user `@Int_SORSE`.

## Requirements

- Python 3
- Create an App on Twitter's developer portal
- The following environment variables must be set and be readable by Python's `os.environ`:
  - `API_KEY`: The Twitter API Key
  - `API_KEY_SECRET`: The Twitter API Key secret
  - `ACCESS_TOKEN`: The Twitter Access Token
  - `ACCESS_TOKEN_SECRET`: The Twitter Access Token secret
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

You can also change the `RETWEET_USER` in `bot.py` if you want to trigger the bot from a different account.
You can store the environment variables in a file `.env` and load them from it with `source .env`:

```bash
export API_KEY=... # Use your own API key, etc.
export API_KEY_SECRET=...
export ACCESS_TOKEN=...
export ACCESS_TOKEN_SECRET=...
```

Note that even on your own machine, you should limit who can read/edit this file, at least `chmod 0700 .env`.

## Deploy to Heroku

1. Get an account on <https://heroku.com>.
2. Install the [`heroku` command line tool](https://devcenter.heroku.com/articles/heroku-cli#download-and-install).
3. Login to Heroku via the command line tool with `heroku login`.
4. In the root of the repository, run `heroku create` which will set up a Heroku app and create a `heroku` remote for the repository.
5. Create the file containing the last seen tweet (see above) and commit it to git:  
   `echo "1234567890..." > last_seen.txt && git add last_seen.txt && git commit -m "Add last seen file"`
6. Set the environment variables for the Heroku app:
   1. `heroku config:set API_KEY=...`
   2. `heroku config:set API_KEY_SECRET=...`
   3. `heroku config:set ACCESS_TOKEN=...`
   4. `heroku config:set ACCESS_TOKEN_SECRET=...`
7. Deploy the app by running `git push heroku main`.
8. Start the worker on Heroku by running `heroku ps:scale worker=1`.

You can check whether the bot has been deployed and is running with `heroku logs --tail`.

## License

MIT License

Copyright (c) 2020 Stephan Druskat

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.