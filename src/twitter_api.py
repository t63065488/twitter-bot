from dotenv import dotenv_values
import tweepy
import logging


class TwitterApi:
    config = dotenv_values(".env")
    MAX_TWEET_LEN = int(config.get("MAX_TWEET_LEN", "280"))
    client = tweepy.Client(consumer_key=config.get("API_KEY"), consumer_secret=config.get(
        "API_KEY_SECRET"), access_token=config.get("ACCESS_TOKEN"), access_token_secret=config.get("ACCESS_TOKEN_SECRET"))

    def post_tweet(self, tweet):
        tweets = []
        if len(tweet) > self.MAX_TWEET_LEN:
            logging.info("Tweet exceeds length limit, processing.")
            tweets = self._format_tweets(tweet)
        else:
            logging.info(
                "Tweet does not exceed length limit, proceeding without processing.")
            tweets = [tweet]
        for tweet in tweets:
            self.client.create_tweet(text=tweet)

    def post_tweet_from_files(self, paths: list[str]):
        self.post_tweet(self._load_and_concat(paths))

    def _load_and_concat(self, paths: list[str]):
        text = ""
        for path in paths:
            text += open(path, "r").read() + "\n"
        return text

    def _format_tweets(self, tweets: str):
        n = self.MAX_TWEET_LEN - 10
        template = ("\n\n({current}/{max})")
        processed = [tweets[i:i+n] for i in range(0, len(tweets), n)]
        for i, tweet in enumerate(processed):
            processed[i] = tweet + \
                template.format(current=i+1, max=len(processed))
        return processed
