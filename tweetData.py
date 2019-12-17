from services.twitter import Twitter
import json

def dumpTwitterTimeline():
    twitter = Twitter()
    timeline = twitter.getHomeTimeline()

    with open('nltk/tweet.json', 'w') as outfile:
        json.dump(timeline, outfile)


with open('nltk/tweet.json') as json_file:
    data = json.load(json_file)

for tweet in data:
    print (tweet['text'])
    print ("\n")