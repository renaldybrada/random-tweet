from services.twitter import Twitter
import pyfiglet

class Browse:
    #  List of Menu
    menus = [
        { 'id' : 0, 'title' : 'Read my home timeline' },
        { 'id' : 1, 'title' : 'Stalk someone timeline' },
        { 'id' : 2, 'title' : 'Retweet a tweet' },
        { 'id' : 3, 'title' : 'Like a tweet' },
        { 'id' : 4, 'title' : 'Reply a tweet' },
        { 'id' : 5, 'title' : 'Tweet to the world' },
        { 'id' : 6, 'title' : 'Trending near me' },
        { 'id' : 7, 'title' : 'Trending worldwide' },
        { 'id' : 99, 'title' : 'Get out from here! my boss is coming' }
    ]

    # Timeline Pagination
    tweet_limit = 200
    per_page = 5

    # Twitter constructor
    twitter = Twitter() 

    def printTitle(self, title):
        text = pyfiglet.figlet_format(title)
        print(text)

    # Showing available menu
    def showMenu(self):
        menus = self.menus
        print("I want to ..")
        for menu in menus:
            item = '[' + str(menu['id']) + '] ' + menu['title']
            if menu['id'] == 99 :
                print("")
            print(item)

        print("")
        chooseMenu = input('What do you want ? [0, 1, 2] : ')
        print("")
        
        self.menuController(chooseMenu)

    # Controlling menu to function
    def menuController(self, idMenu):
        if idMenu == "0" :
            self.showTimeline()
        elif idMenu == "1" :
            screen_name = input('whom you will stalk? [type username] ')
            self.showTimeline(False, screen_name)
        elif idMenu == "2" :
            tweet_id = input('which tweet you want to retweet [type tweet id] ')
            self.twitter.retweet(tweet_id)
            print('')
        elif idMenu == "3" :
            tweet_id = input('which tweet you want to like [type tweet id] ')
            self.twitter.likeTweet(tweet_id)
            print('')
        elif idMenu == "4" :
            tweet_id = input('which tweet you want to reply [type tweet id] ')
            message = input('type your reply : ')
            self.twitter.replyTweet(message, tweet_id)
            print('')
        elif idMenu == "5" :
            message = input('type your tweet : ')
            self.twitter.postTweet(message)
            print('')
        elif idMenu == "6" :
            self.showTrending(False)
        elif idMenu == "7" :
            self.showTrending()
        elif idMenu == "99" :
            exit()
        else:
            print('whoops! please select menu by typing its index')
            print("")
            self.showMenu()

        print("")

    # showing timeline
    def showTimeline(self, isHome = True, screen_name = ''):
        if isHome :
            self.printTitle('timeline')
            timeline = self.twitter.getHomeTimeline(self.tweet_limit)
        else :
            if screen_name == '' :
                print('screen name not specified')
                self.showMenu()
            else:
                self.printTitle(screen_name + " timeline's")
                timeline = self.twitter.getUserTimeline(screen_name, self.tweet_limit)

        # pagination
        current_page = 0
        last_page = len(timeline) / self.per_page
        
        while current_page < last_page :
            firstIndex = current_page * self.per_page
            lastIndex = firstIndex + self.per_page
            print('timeline page ' + str(current_page + 1))
            print('') 
            showTimeline = timeline[firstIndex:lastIndex]
            
            for post in showTimeline :
                print('id : ' + post['id_str'])
                print('username : ' + post['user']['screen_name'])
                print(post['text'])
                print("")
                print(str(post['retweet_count']) + ' retweet, ' + str(post['favorite_count']) + ' like')
                print(post['created_at'])
                print("====================================================================================================================")
                print("")
                
            action = input('press any key to continue or "m" to back to menu.. ')
            print("")
            if(action == "m"):
                self.showMenu()
                break

            current_page += 1

    def showTrending(self, isWorldwide = True):
        trends = []
        if isWorldwide :
            self.printTitle('Trending WW')
            trends = self.twitter.getWorldWideTrend()
        else :
            self.printTitle('Trending near you')
            trends = self.twitter.getClosestTrend()
        
        # pagination
        current_page = 0
        last_page = len(trends) / self.per_page

        while current_page < last_page :
            firstIndex = current_page * self.per_page
            lastIndex = firstIndex + self.per_page
            print('trend page ' + str(current_page + 1))
            print('') 
            showTrends = trends[firstIndex:lastIndex]

            for trend in showTrends:
                print(trend['name'])
                trend_volume = 0
                if trend['tweet_volume'] != None :
                    trend_volume = trend['tweet_volume']
                print(str(trend_volume) + ' tweets')
                print('==================================')

            action = input('press any key to continue or "m" to back to menu.. ')
            print("")
            if(action == "m"):
                self.showMenu()
                break

            current_page += 1


# show title
twitter_title = pyfiglet.figlet_format("Twitter-CLI", font = "slant")
print(twitter_title)

browse = Browse()
while True:
    try :
        browse.showMenu()
    except :
        print('something went wrong, if this happen again please restart the app')
        print('')
        browse.showMenu()