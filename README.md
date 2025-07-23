# Generador de Contenido para Twitter

Generar automáticamente tweets creativos, relevantes y atractivos para una cuenta de Twitter.
Personalizar el contenido según temas, tendencias o eventos actuales.
Optimizar los tweets para maximizar el engagement (uso de hashtags, menciones, longitud adecuada).

---

## Características

- Generación automática de tweets a partir de prompts temáticos.
- Post-procesamiento para agregar hashtags, limpiar y acortar tweets.
- Memoria para evitar publicar contenido repetido o muy similar.
- Integración con la API de Twitter para publicación directa.
- Modularidad y facilidad de extensión.

---

## Configuración

1. **Clona el repositorio y entra en la carpeta:**
   ```bash
   git clone https://github.com/franfigueroa/GeneradorDeTweets.git
   cd GeneradorDeTweets
   ```

2. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configura tus claves de API en un archivo `.env`:**
   ```
   OPENAI_API_KEY=sk-...
   TWITTER_API_KEY=...
   TWITTER_API_SECRET=...
   TWITTER_ACCESS_TOKEN=...
   TWITTER_ACCESS_TOKEN_SECRET=...
   ```

4. **Edita o agrega tus propios prompts en `data/prompts/`.**

---

## Uso

Para generar y publicar un tweet:

```bash
python src/main.py
```

Puedes modificar el tipo de tweet, hashtags y otros parámetros editando `main.py` o pasándolos como argumentos.

---

## Pruebas

Para ejecutar las pruebas unitarias:

```bash
pytest
```

---

## Personalización

- Agrega nuevos tipos de prompts en `data/prompts/`.
- Ajusta el post-procesamiento en `src/postprocessing.py`.
- Modifica la lógica de memoria en `src/memory.py`.

---
## Mejoras Futuras

- Se planea agregar una funcionalidad para que el usuario pueda seleccionar fácilmente el tipo de tweets que desea publicar (motivacional, noticia, humor, etc.) sin modificar el código.
- Se implementará una interfaz más amigable para la configuración y el uso del generador.
- Otras mejoras para facilitar la personalización y la experiencia de usuario. 

---
## Licencia

MIT




