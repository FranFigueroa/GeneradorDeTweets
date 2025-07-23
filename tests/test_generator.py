from src.generator import cargar_prompt, generar_tweet

def test_cargar_prompt():
    prompt = cargar_prompt("motivacional")
    assert isinstance(prompt, str)
    assert len(prompt) > 0

def test_generar_tweet():
    prompt = "Crea un tweet motivacional para empezar el día."
    tweet = generar_tweet(prompt)
    assert isinstance(tweet, str)
    assert len(tweet) > 0
