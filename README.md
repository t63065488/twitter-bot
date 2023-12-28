# Twitter Bot
Short Python script to automate posting a tweet (Xeet?).

## Installing Dependencies
To be able to run the core project, from the root directory, run:
```
pip install .
```

To be able to run the tests, from the root directory, run:
```
pip install .[test]
```

## Runing the Script
This script expects file paths to be passed on the CLI, which in turn are read and processed (if the length exceeds the maximum tweet length). To do this, the tweepy library requires the following environment variables to be set in the local .env file:

- API_KEY -> This is your consumer key, as generated when creating an app on the Twitter developer portal.
- API_KEY_SECRET -> The corresponding secret. 
- ACCESS_TOKEN -> A generated oAuth2 access token, retrieved via the Twitter developer portal from your app.
- ACCESS_TOKEN_SECRET -> The corresponding secret.

For more information on these tokens, and how to generate them, see: https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api

By default, the maximum tweet length is set to 280 characters. This can be amended by setting the key MAX_TWEET_LEN in your .env file. 

Assuming these variables are present, the script can be executed, from the root directory, by running: 
```
python src/twitter_bot/main.py PATH_TO_FILE_ONE PATH_TO_FILE_TWO ...
```