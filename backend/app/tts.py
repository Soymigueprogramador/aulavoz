# Importacion de librerias necesarias
import asyncio
import edge_tts
import os

# Funcion para generar los audios
async def generar_audio( texto, salida ):
    os.makedirs(os.path.dirname(salida), exist_ok=True)

    communicate = edge_tts.Communicate(
        text=texto,
        voice="es-AR-ElenaNeural"
    )

    await communicate.save(salida)

# Funcion para convertir el texto en audio
def convertir_texto_audio( texto, salida ):
    asyncio.run(generar_audio(texto, salida))