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

# use pandas to read the quotes out of the csv file. Pandas was the most efficient way to do this that I found.
quote = []
quotes = pd.read_csv('quote_text_tweets.csv')

# a random quote will be chosen and tweeted each time the script runs
def tweet_stoic_quote():
    api.update_status(random.choice(quotes['QUOTE']), flush=True)


tweet_stoic_quote()
