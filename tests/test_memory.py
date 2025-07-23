from src.postprocessing import postprocesar_tweet

def test_postprocesar_tweet():
    tweet = "¡Hola mundo!"
    hashtags = ["#Test", "#Python"]
    tweet_final = postprocesar_tweet(tweet, hashtags)
    assert "#Test" in tweet_final
    assert "#Python" in tweet_final
    assert len(tweet_final) <= 280
