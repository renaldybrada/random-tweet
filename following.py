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
def isWorthFollowing(follower):
    maxFollower = 500
    followerGap = follower['friends_count'] - follower['followers_count']
    gapLimit = 20

    if (follower['followers_count'] < follower['friends_count']) and (follower['followers_count'] < maxFollower) and followerGap >= gapLimit :
        return True
    else :
        return False

def selectedTwitterAccount():
    twitterScreenNames = ["infomalang", "infobdg", "VICE_ID", "potretlawas", "NUgarislucu", "KatolikG", "mojokdotco", "ThelIluminatii"]
    # twitterScreenNames = ["infomalang", "infomalang", "infomalang"]
    randIndex = random.randrange(0, 3, 1)
    return twitterScreenNames[randIndex]

def populatingFollowingCandidate(twitterAccount, cursor=-1):
    candidate = []

    followersResponse = twitter.getFollowersList(twitterAccount, cursor=cursor)
    print ("observing " + twitterAccount + "'s followers.. \n")

    followers = followersResponse['users']
    for follower in followers:
        if isFollowed(follower) :
            continue
        elif isWorthFollowing(follower) :
            screen_name = follower['screen_name']
            print(screen_name)
            if( type(screen_name) != None ):
                candidate.append(screen_name)
        else :
            continue

    nextCursor = followersResponse['next_cursor']
    if((len(candidate) == 0) and (nextCursor != 0)):
        populatingFollowingCandidate(twitterAccount, cursor=nextCursor)
    else:
        return candidate

try:
    twitter = Twitter()
    twitterAccount = selectedTwitterAccount()
    candidate = populatingFollowingCandidate(twitterAccount)

    for user in candidate:
        twitter.followAccount(user)
except Exception as e:
    print('something went wrong: '+ str(e))


# print (json.dumps(followers, indent=4, sort_keys=True))