import os
from openai import OpenAI

def cargar_prompt(tipo):
    with open(f"data/prompts/{tipo}.txt", "r", encoding="utf-8") as f:
        return f.read()

def generar_tweet(prompt, hashtags=""):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # O el modelo que prefieras
        messages=[
            {"role": "system", "content": "Eres un generador de tweets creativo y conciso."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=60,
        temperature=0.8,
    )
    tweet = response.choices[0].message.content.strip()
    if hashtags:
        tweet = f"{tweet} {hashtags}"
    return tweet



# Prueba 
if __name__ == "__main__":
    prompt = cargar_prompt("motivacional")
    hashtags = "#Motivación #BuenosDías"
    tweet = generar_tweet(prompt, hashtags)
    print("Tweet generado:", tweet)
