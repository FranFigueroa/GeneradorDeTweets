import tweepy
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

API_KEY = os.getenv("TWITTER_API_KEY")
API_SECRET = os.getenv("TWITTER_API_SECRET")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

def get_twitter_client():
    auth = tweepy.OAuth1UserHandler(
        API_KEY, API_SECRET,
        ACCESS_TOKEN, ACCESS_TOKEN_SECRET
    )
    api = tweepy.API(auth)
    return api

def post_tweet(text):
    api = get_twitter_client()
    status = api.update_status(status=text)
    return status

# Prueba
if __name__ == "__main__":
    tweet = "¡Hola, mundo! #GenerativeAI"
    status = post_tweet(tweet)
    print("Tweet publicado:", status.text)
