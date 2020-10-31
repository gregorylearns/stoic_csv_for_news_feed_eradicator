import tweepy
from datetime import datetime, timedelta
from threading import Timer
import random
import pandas as pd
from credentials import *


# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

# Create API object
api = tweepy.API(auth)

# x = datetime.today()
# y = x.replace(day=x.day, hour=1, minute=0, second=0, microsecond=0) + timedelta(days=1)
# delta_t = y-x
# secs = delta_t.total_seconds()

quote = []
quotes = pd.read_csv('quote_text_tweets.csv')


def tweet_stoic_quote():
    api.update_status(random.choice(quotes['QUOTE']), flush=True)


# t = Timer(secs, tweet_stoic_quote)
# t.start()

tweet_stoic_quote()