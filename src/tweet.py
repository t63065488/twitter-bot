import sys
import tweepy
import logging
from dotenv import dotenv_values

config = dotenv_values(".env")

MAX_TWEET_LEN = int(config.get("MAX_TWEET_LEN", "280"))


def main(args):
    text = load_and_concat(args)
    tweets = []
    if len(text) > MAX_TWEET_LEN:
        logging.info("Tweet exceeds length limit, processing.")
        tweets = process_tweets(text)
    else:
        logging.info(
            "Tweet does not exceed length limit, proceeding without processing.")
        tweets = [text]
    post_tweet(tweets)


def load_and_concat(paths: list[str]) -> str:
    text = ""
    for path in paths:
        text += open(path, "r").read() + "\n"
    return text


def process_tweets(tweets: str) -> list[str]:
    n = MAX_TWEET_LEN - 10
    template = ("\n\n({current}/{max})")
    processed = [tweets[i:i+n] for i in range(0, len(tweets), n)]
    for i, tweet in enumerate(processed):
        processed[i] = tweet + template.format(current=i+1, max=len(processed))
    return processed


def post_tweet(tweets: list[str]):
    client = tweepy.Client(consumer_key=config.get("API_KEY"), consumer_secret=config.get(
        "API_KEY_SECRET"), access_token=config.get("ACCESS_TOKEN"), access_token_secret=config.get("ACCESS_TOKEN_SECRET"))
    for tweet in tweets:
        client.create_tweet(text=tweet)


if __name__ == "__main__":
    main(sys.argv[1:])
