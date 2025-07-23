import os
import json
from difflib import SequenceMatcher

MEMORY_FILE = "data/tweet_memory.json"
SIMILARITY_THRESHOLD = 0.85 
def cargar_memoria():
    if not os.path.exists(MEMORY_FILE):
        return []
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def guardar_memoria(memoria):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memoria, f, ensure_ascii=False, indent=2)

def es_repetido(nuevo_tweet, memoria):
    for tweet in memoria:
        if nuevo_tweet.strip() == tweet.strip():
            return True
        # Chequeo de similitud
        ratio = SequenceMatcher(None, nuevo_tweet, tweet).ratio()
        if ratio > SIMILARITY_THRESHOLD:
            return True
    return False

def agregar_a_memoria(nuevo_tweet):
    memoria = cargar_memoria()
    memoria.append(nuevo_tweet)
    guardar_memoria(memoria)

# Ejemplo de uso
if __name__ == "__main__":
    tweet = "¡Buenos días a todos! Hoy es un gran día para aprender sobre IA."
    memoria = cargar_memoria()
    if es_repetido(tweet, memoria):
        print("Este tweet ya fue publicado o es muy similar a uno anterior.")
    else:
        agregar_a_memoria(tweet)
        print("Tweet guardado en memoria.")
