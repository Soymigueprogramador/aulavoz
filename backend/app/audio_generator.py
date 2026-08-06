from pathlib import Path
from app.tts import convertir_texto_audio

def generar_audios(carpeta_secciones):
    carpeta_secciones = Path(carpeta_secciones)

    carpeta_audio = carpeta_secciones / "audio"
    carpeta_audio.mkdir(exist_ok=True)

    archivos = sorted(carpeta_secciones.glob("*.txt"))

    cantidad = len(archivos)

    for indice, archivo in enumerate(archivos, start=1):
        salida = carpeta_audio / f"{archivo.stem}.mp3"

        print(f"[{indice}/{cantidad}] Generando: {archivo.name}")

        texto = archivo.read_text(encoding="utf-8")

        convertir_texto_audio(
            texto,
            str(salida)
        )

    print()
    print(f"✓ Se generaron {cantidad} audios.")
    print(f"✓ Carpeta: {carpeta_audio}")

    return carpeta_audio