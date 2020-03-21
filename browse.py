from services.twitter import Twitter
import pyfiglet

class Browse:
    #  List of Menu
    menus = [
        { 'id' : 0, 'title' : 'Read my timeline' },
        { 'id' : 1, 'title' : 'Retweet a tweet' },
        { 'id' : 2, 'title' : 'Like a tweet' },
        { 'id' : 3, 'title' : 'Stalk someone timeline' },
        { 'id' : 99, 'title' : 'Get out from here! my boss is watching' }
    ]

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
        
        self.menuController(int(chooseMenu))

    # Controlling menu to function
    def menuController(self, idMenu):
        if idMenu == 0 :
            self.showHomeTimeline()
        elif idMenu == 1 :
            print('retweet under construction')
        elif idMenu == 2 :
            print('like under construction')
        elif idMenu == 3 :
            print('stalk under construction')
        elif idMenu == 99 :
            exit()
        print("")

    # showing timeline
    def showHomeTimeline(self):
        twitter = Twitter()
        timeline = twitter.getHomeTimeline(5)
        for post in timeline :
            print('username : ' + post['user']['screen_name'])
            print(post['text'])
            print("")
            print(str(post['retweet_count']) + ' retweet, ' + str(post['favorite_count']) + ' like')
            print(post['created_at'])
            print("====================================================================================================================")
            print("")


# show title
twitter_title = pyfiglet.figlet_format("Twitter-CLI")
print(twitter_title)

browse = Browse()
while True:
    browse.showMenu()

