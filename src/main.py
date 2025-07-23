from generator import cargar_prompt, generar_tweet
from postprocessing import postprocesar_tweet
from memory import cargar_memoria, es_repetido, agregar_a_memoria
from twitter_api import post_tweet

if __name__ == "__main__":
    tipo = "motivacional"  
    hashtags = ["#Motivación", "#IA"]

    prompt = cargar_prompt(tipo)
    tweet_generado = generar_tweet(prompt)
    tweet_final = postprocesar_tweet(tweet_generado, hashtags)

    memoria = cargar_memoria()
    if es_repetido(tweet_final, memoria):
        print("Este tweet ya fue publicado o es muy similar a uno anterior. No se publicará.")
    else:
        post_tweet(tweet_final)
        agregar_a_memoria(tweet_final)
        print("Tweet publicado y guardado en memoria.")
