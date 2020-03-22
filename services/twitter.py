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

    def getHomeTimeline(self, count=200):
        timeline = self.twitter.get_home_timeline(count=count)
        return timeline
    
    def getUserTimeline(self, screen_name, count=200):
        timeline = self.twitter.get_user_timeline(screen_name=screen_name, count=count)
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

    def getClosestTrend(self):
        locationResponse = requests.get('https://freegeoip.app/json/')
        location = locationResponse.json()
        locationTwitter = self.twitter.get_closest_trends(lat=location['latitude'], long=location['longitude'])
        trends = self.twitter.get_place_trends(id=int(locationTwitter[0]['woeid']))
        trends = trends[0]['trends']
        return trends

    def getWorldWideTrend(self):
        trends = self.twitter.get_place_trends(id=1, exclude="words")
        trends = trends[0]['trends']
        return trends

    def selectHashtagFromTrend(self, trends):
        hashtagTrend = ""
        for trend in trends:
            if (trend['name'].find('#') != -1):
                hashtagTrend = trend['name']
                break 
        return hashtagTrend

    def likeTweet(self, tweet_id):
        self.twitter.create_favorite(id=tweet_id)
        print(tweet_id + " liked!")

    def getFollowersList(self, screen_name, cursor=-1):
        fetchCount = 5
        followers = self.twitter.get_followers_list(screen_name=screen_name, count=fetchCount, cursor=cursor)
        return followers

    def followAccount(self, screen_name):
        self.twitter.create_friendship(screen_name=screen_name)
        print ("following : " + screen_name)