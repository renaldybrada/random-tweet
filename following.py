from services.twitter import Twitter
import random
import json

def isFollowed(follower):
    if follower['follow_request_sent'] or follower['following']:
        return True
    else:
        return False

# checking is follower has followers < following
# checking max followers
# checking follower gap
# checking last activity <-- not done
def isWorthFollowing(follower):
    maxFollower = 500
    followerGap = follower['friends_count'] - follower['followers_count']
    gapLimit = 20

    if (follower['followers_count'] < follower['friends_count']) and (follower['followers_count'] < maxFollower) and followerGap >= gapLimit :
        return True
    else :
        return False

twitterScreenNames = ["infomalang", "infobdg", "VICE_ID", ""]
randIndex = random.randrange(0, 3, 1)

twitter = Twitter()
followersResponse = twitter.getFollowersList(twitterScreenNames[randIndex])
print (twitterScreenNames[randIndex])
followers = followersResponse['users']
for follower in followers:
    if isFollowed(follower) :
        continue
    elif isWorthFollowing(follower) :
        print (follower['screen_name'])
    else :
        continue

# print (json.dumps(followers, indent=4, sort_keys=True))