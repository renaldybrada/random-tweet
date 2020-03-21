from services.twitter import Twitter
import pyfiglet

# show title
twitter_title = pyfiglet.figlet_format("Twitter-CLI")
print(twitter_title)

def showHomeTimeline():
    twitter = Twitter()
    timeline = twitter.getHomeTimeline(10)
    for post in timeline :
        print('username : ' + post['user']['screen_name'])
        print(post['text'])
        print("")
        print(str(post['retweet_count']) + ' retweet, ' + str(post['favorite_count']) + ' like')
        print(post['created_at'])
        print("====================================================================================================================")
        print("")

showHomeTimeline()

