import base64
from pprint import pprint
import requests
import json
from twython import Twython

class Twitter:
    twitter = None

    def __init__(self):
        twitter_credential = self.importCredential()
        self.twitter = Twython(
            twitter_credential['api_key'],
            twitter_credential['api_secret_key'],
            twitter_credential['access_token'],
            twitter_credential['access_token_secret']
        )  

    def importCredential(self):
        twitter_credential = {}
        with open('credentials.json') as f:
            credential = json.load(f)
        twitter_credential = credential['twitter'] 
        return twitter_credential

    def getHomeTimeline(self):
        timeline = self.twitter.get_home_timeline(count=100)
        return timeline
    
    def getUserTimeline(self, screen_name):
        timeline = self.twitter.get_user_timeline(screen_name=screen_name)
        return timeline
        
    def postTweet(self, message):
        self.twitter.update_status(status=message)
        print("Tweeted: " + message)

    def replyTweet(self, message, tweet_id):
        self.twitter.update_status(status=message, in_reply_to_status_id=tweet_id)
        print("Tweeted reply: " + message)

    def retweet(self, tweet_id):
        self.twitter.retweet(id=tweet_id)
        print(tweet_id + " Retweeted!")