# mytwitterbot.py
# IAE 101, Fall 2021
# Project 04 - Building a Twitterbot
# Name: Christopher Rosales
# netid: CMROSALES
# Student ID: 114328928

import sys
import time, random
import json
import simple_twit
import requests
import logging
import tweepy
from time import sleep
from keys import *


logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)
logger.setLevel(logging.INFO)

# Project 04 Exercises
    
# Exercise 1 - Get and print 10 tweets from your home timeline
# For each tweet, print the tweet ID, the author's name,
# the author's screen_name, the tweet creation date, and the
# tweet full_text
def exercise1(api):
    tweets = []
    tweets = simple_twit.get_home_timeline(api, 10)
    count = 1
    for tweet in tweets:
        print("%d. Tweet ID: %s; Author's Name: %s; Author's Screen Name: %s; Tweet Creation Date: %s; Tweet Full Text: %s"%(count,tweet.id,tweet.author.name,tweet.author.screen_name,tweet.created_at.strftime("%m/%d/%Y, %H:%M:%S"),tweet.full_text))
        count += 1


# Exercise 2 - Get and print 10 tweets from another user's timeline
# For each tweet, print the tweet ID, the author's name,
# the author's screen_name, the tweet creation date, and the
# tweet full_text
def exercise2(api):
    tweets = []
    tweets = simple_twit.get_user_timeline(api, "IAE101_ckane", 10)
    count = 1
    for tweet in tweets:
        print("%d. Tweet ID: %s; Author's Name: %s; Author's Screen Name: %s; Tweet Creation Date: %s; Tweet Full Text: %s"%(count,tweet.id,tweet.author.name,tweet.author.screen_name,tweet.created_at.strftime("%m/%d/%Y, %H:%M:%S"),tweet.full_text))
        count += 1


# Exercise 3 - Post 1 tweet to your timeline.
def exercise3(api):
    text = "TwitKarma"
    simple_twit.send_tweet(api, text)


# Exercise 4 - Post 1 media tweet to your timeline.
def exercise4(api):
    text = "TwitKarma"
    simple_twit.send_media_tweet(api, text, "TwitKarma.png")

def twitterbot():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    for tweet in tweepy.Cursor(api.search_tweets, q='#sonic').items(5):
        try:
            print('\nRetweet Bot found tweet by @' + tweet.user.screen_name + '. ' + 'Attempting to retweet.')

            tweet.retweet()
            print('Retweet published successfully.')
            sleep(10)
        except tweepy.TweepError as error:
            print('\nError. Retweet not successful. Reason: ')
            print(error.reason)

        except StopIteration:
            break

if __name__ == "__main__":
    #exercise1(apitwit)
    #exercise2(apitwit)
    #exercise3(apitwit)
    #exercise4(apitwit)
    twitterbot()
