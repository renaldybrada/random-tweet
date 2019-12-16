from services.twitter import Twitter
from services.quotes import Quotes
import random

def randomTweet():
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


def randomRetweet():
    twitter = Twitter()
    timeline = twitter.getHomeTimeline()
    randIndex = random.randrange(0, 100, 1)
    tweet_id = timeline[randIndex]['id_str']
    twitter.retweet(tweet_id)


randomRetweet()
# randomTweet()


