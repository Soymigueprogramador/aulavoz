# Importacion de archivo necesario
from app.tts import convertir_texto_audio

# Texto para hacer la prueba de la conversion
texto = """
Hola.

Esta es una prueba del proyecto AulaVoz.

Si estás escuchando este audio significa que la fase cinco funciona correctamente.
"""

# Le indicamos la ruta y el nombre del archivo que convertimos
convertir_texto_audio(texto, "../output/prueba.mp3")

# Aviso de que el audio fue generado
print("AUDIO CREADO")