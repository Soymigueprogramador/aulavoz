from pathlib import Path

def separar_documentos(secciones, carpeta_salida):
    carpeta = Path(carpeta_salida)
    carpeta.mkdir(parents=True, exist_ok=True)

    archivos_creados = []

    for i, seccion in enumerate(secciones, start=1):
        titulo = seccion["titulo"]
        contenido = seccion["contenido"]

        nombre_archivo = f"{i:02d} - {titulo}.txt"
        ruta_archivo = carpeta / nombre_archivo

        ruta_archivo.write_text(
            contenido,
            encoding="utf-8"
        )

        archivos_creados.append(ruta_archivo)

    return archivos_creados 