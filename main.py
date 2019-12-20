from services.twitter import Twitter
from services.quotes import Quotes
import random

def randomTweet():
    try:
        twitter = Twitter()
        quotes = Quotes()

        # randoming tweet type
        quoteTypes = ["dad-jokes", "advices", "famous-quote"]
        randIndex = random.randrange(0, 3, 1)
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

        # combining message and trending topic hashtag
        hashtag = twitter.selectHashtagFromTrend(trends)
        message = message + " " + hashtag

        twitter.postTweet(message)
    except:
        randomTweet()


def randomRetweet(likeTweet=True):
    try:
        twitter = Twitter()
        timeline = twitter.getHomeTimeline()
        randIndex = random.randrange(0, 200, 1)
        tweet_id = timeline[randIndex]['id_str']
        
        twitter.retweet(tweet_id)

        if(likeTweet):
            twitter.likeTweet(tweet_id)
        
    except:
        randomRetweet()

idx = random.randrange(0, 21, 1)
if(idx % 3 == 0):
    randomRetweet()
elif(idx % 3 == 1):
    randomRetweet(likeTweet=False)
else:
    randomTweet()


