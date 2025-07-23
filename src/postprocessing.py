import re

MAX_TWEET_LENGTH = 280

def limpiar_texto(texto):
    """Elimina espacios extra y caracteres no deseados."""
    texto = texto.strip()
    texto = re.sub(r'\s+', ' ', texto)
    return texto

def agregar_hashtags(tweet, hashtags):
    """Agrega hashtags al final del tweet, asegurando que no exceda el límite."""
    hashtags_str = " ".join(hashtags)
    tweet_con_hashtags = f"{tweet} {hashtags_str}".strip()
    if len(tweet_con_hashtags) > MAX_TWEET_LENGTH:
        # Si pasa, recorta el tweet para dejar espacio a los hashtags (probar)
        espacio_para_tweet = MAX_TWEET_LENGTH - len(hashtags_str) - 1
        tweet = tweet[:espacio_para_tweet].rstrip()
        tweet_con_hashtags = f"{tweet} {hashtags_str}".strip()
    return tweet_con_hashtags

def acortar_tweet(tweet):
    """Recorta el tweet si excede el límite de caracteres."""
    if len(tweet) > MAX_TWEET_LENGTH:
        return tweet[:MAX_TWEET_LENGTH-1] + "…"
    return tweet

def postprocesar_tweet(tweet, hashtags=None):
    """Limpia, acorta y agrega hashtags al tweet."""
    tweet = limpiar_texto(tweet)
    if hashtags:
        tweet = agregar_hashtags(tweet, hashtags)
    tweet = acortar_tweet(tweet)
    return tweet

# Ejemplo de uso
if __name__ == "__main__":
    tweet = "  ¡Buenos días a todos! Hoy es un gran día para aprender sobre IA.  "
    hashtags = ["#IA", "#Aprendizaje", "#Motivación"]
    tweet_final = postprocesar_tweet(tweet, hashtags)
    print("Tweet final:", tweet_final)
    print("Longitud:", len(tweet_final))
