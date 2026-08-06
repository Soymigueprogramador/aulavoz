from pathlib import Path
import re

# Funcion para separar el documento
def separar_documentos(secciones, carpeta_salida):
    # Guarda cada sección como un archivo de texto independiente.

    carpeta = Path(carpeta_salida)
    carpeta.mkdir(parents=True, exist_ok=True)

    archivos_creados = []

    for i, seccion in enumerate(secciones, start=1):
        titulo = seccion.get("titulo", "Sin título")
        contenido = seccion.get("contenido", "")

        titulo_limpio = limpiar_nombre_archivo(titulo)

        nombre_archivo = f"{i:02d} - {titulo}.txt"
        ruta_archivo = carpeta / nombre_archivo

        ruta_archivo.write_text(
            contenido,
            encoding="utf-8"
        )

        archivos_creados.append(ruta_archivo)

    return archivos_creados

# Funcion para limpiar el nombre del archivo
def limpiar_nombre_archivo(nombre):
    # Convierte un título en un nombre de archivo válido para Windows.

    # Reemplaza los caracteres invalidos por un _
    nombre = re.sub(r'[<>:"/\\|?*]', "_", nombre)

    # Elimina espacion al principio y al final del titulo
    nombre = nombre.strip()

    return nombre