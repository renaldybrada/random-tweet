import requests
import json

class Quotes:
    def randomDadJokes(self):
        baseUrl = "https://icanhazdadjoke.com/"
        headers = {"Accept": "application/json"}
        response = requests.get(baseUrl, headers=headers)
        theJoke = response.json()['joke'] 
        return theJoke

    def randomAdvices(self):
        baseUrl = "https://api.adviceslip.com/advice"
        response = requests.get(baseUrl)
        theAdvice = response.json()['slip']['advice'] 
        return theAdvice

    def randomFamousQuote(self):
        baseUrl = "https://quote-garden.herokuapp.com/quotes/random"
        response = requests.get(baseUrl)
        theQuote = response.json()['quoteText']
        theAuthor = response.json()['quoteAuthor']
        if(theAuthor == ""):
            theAuthor = "anonymous"
        return "'" + theQuote + "' - " + theAuthor 