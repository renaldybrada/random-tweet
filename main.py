from services.twitter import Twitter
from services.quotes import Quotes
import random

def randomTweet():
    try:
        twitter = Twitter()
        quotes = Quotes()
        quoteTypes = ["dad-jokes", "advices", "famous-quote"]
        randIndex = random.randrange(0, 2, 1)
        
        if (quoteTypes[randIndex] == "dad-jokes"):
            message = quotes.randomDadJokes()
        elif (quoteTypes[randIndex] == "advices"):
            message = quotes.randomAdvices()
        else:
            message = quotes.randomFamousQuote()
        
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


