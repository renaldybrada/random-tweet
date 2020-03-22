from services.twitter import Twitter
import pyfiglet

class Browse:
    #  List of Menu
    menus = [
        { 'id' : 0, 'title' : 'Read my timeline' },
        { 'id' : 1, 'title' : 'Retweet a tweet' },
        { 'id' : 2, 'title' : 'Like a tweet' },
        { 'id' : 3, 'title' : 'Stalk someone timeline' },
        { 'id' : 4, 'title' : 'Tweet to the world' },
        { 'id' : 99, 'title' : 'Get out from here! my boss is watching' }
    ]

    # Tweet Pagination
    tweet_limit = 200
    per_page = 5

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
            self.showHomeTimeline()
        elif idMenu == "1" :
            print('retweet under construction')
        elif idMenu == "2" :
            print('like under construction')
        elif idMenu == "3" :
            print('stalk under construction')
        elif idMenu == "99" :
            exit()
        else:
            print('whoops!')
            print("")
            self.showMenu()

        print("")

    # showing timeline
    def showHomeTimeline(self):
        self.printTitle('timeline')
    
        twitter = Twitter()
        timeline = twitter.getHomeTimeline(self.tweet_limit)
        
        # pagination
        current_page = 0
        last_page = self.tweet_limit / self.per_page
        
        while current_page != last_page :
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

# show title
twitter_title = pyfiglet.figlet_format("Twitter-CLI", font = "slant")
print(twitter_title)

browse = Browse()
while True:
    browse.showMenu()

