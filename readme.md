# Random Tweet 

In the beginning, this repository was just my playground for exploring python using Twitter API. Its features was super basic 

  - Random tweet something utilizing [Bad Dad Joke API](https://icanhazdadjoke.com/), [Advice API](https://api.adviceslip.com/advice), and [Famous Quote API](https://quote-garden.herokuapp.com/quotes/random)
  - Random liking and retweeting tweet on my (robot account) timeline
  - Random following people

# New Features!

Now you can accessing your account via CLI. Basically the feature is play twitter on your terminal. The key features are :

  - Show your home timeline : including your tweets and your following tweets
  - Show specified user timeline
  - Retweet, like, and reply tweet
  - Post a tweet

All of that features on your terminal!

### Installation

Random Tweet using python 3.*

#### I recommend using virtualenv
```sh
$ cd random-tweet
$ virtualenv venv
$ venv/Scripts/activate
```

#### Installing package requirement

```sh
$ pip install -r
```

#### Twitter credentials

Copy credentials.json.example to credentials.json
```sh
$ cp credentials.json.example credentials.json
```
Then fill that json with your credentials
```sh
{
    "twitter": {
        "api_key" : "your consumer api key",
        "api_secret_key" : "your consumer api secret key",
        "access_token" : "your access token",
        "access_token_secret" : "your access token secret"
    }
}
```
### How To Use
For random tweeting bad dad joke, advice, quote or random like a tweet or random retweeting a tweet. Just run main.py
```sh
$ python main.py
```

Running twitter via command line
```sh
$ python browse.py
```