from services.twitter import Twitter
from services.quotes import Quotes
import random

def randomTweet():
    try:
        twitter = Twitter()
        quotes = Quotes()

        # randoming tweet type
        quoteTypes = ["dad-jokes", "advices", "famous-quote"]
        randIndex = random.randrange(0, 2, 1)
        if (quoteTypes[randIndex] == "dad-jokes"):
            message = quotes.randomDadJokes()
        elif (quoteTypes[randIndex] == "advices"):
            message = quotes.randomAdvices()
        else:
            message = quotes.randomFamousQuote()
        
        # randoming trending topic hashtag
        randIndex = random.randrange(0, 2, 1)
        if(randIndex==1):
            trends = twitter.getWorldWideTrend()
        else:
            trends = twitter.getClosestTrend()
        hashtag = twitter.selectHashtagFromTrend(trends)

        # combining message and trending topic hashtag
        message = message + " " + hashtag

        twitter.postTweet(message)
        print('tweeting : ' + message)
    except:
        randomTweet()


def randomRetweet():
    try:
        twitter = Twitter()
        timeline = twitter.getHomeTimeline()
        randIndex = random.randrange(0, 200, 1)
        tweet_id = timeline[randIndex]['id_str']

        twitter.retweet(tweet_id)
        print("retweeting : " + tweet_id)
    except:
        randomRetweet()

idx = random.randrange(0, 20, 1)
if(idx % 2 == 0):
    randomRetweet()
else:
    randomTweet()


