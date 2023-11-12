import requests

CHUCKNORRIS_URL = 'https://api.chucknorris.io/jokes/random'
DAD_URL = 'https://icanhazdadjoke.com/'

def random_joke_get_method():
    r = requests.get(CHUCKNORRIS_URL).json()
    joke = {'joke' : r["value"]}
    return joke

def random_chuck_joke_function():
    r = requests.get(CHUCKNORRIS_URL).json()
    joke = {'chuck_joke' : r["value"]}
    return joke
    
def random_dad_joke_function():
    
    headers = {
    'Accept': 'application/json',
    }
    r = requests.get(DAD_URL, headers=headers).json()
    
    joke = {'dad_joke' : r["joke"]}
    return joke