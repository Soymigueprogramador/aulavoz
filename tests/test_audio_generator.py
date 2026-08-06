# Importacion de archivos necesarios
from app.audio_generator import generar_audios

print("=" * 60)
print("FASE 6 - GENERAR TODOS LOS AUDIOS")
print("=" * 60)

# Rita donde guardamos la carpeta con los audios
carpeta = "../output/tiende tu cama"

# Llamado a la funcion que genera los audios
generar_audios(carpeta)