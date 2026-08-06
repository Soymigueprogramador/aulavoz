# Importacion de librerias necesarias
from pathlib import Path

# Importacion de archivos necesarios
from app.pdf_extractor import extraer_texto_pdf
from app.section_detector import detectar_secciones
from app.document_splitter import separar_documentos

# Ruta del PDF
ruta_pdf = "../tests/pdfs/Tiende_tu_cama_William_H_McRaven.pdf"

# Pasos del proceso:
# 1 Extraemos el texto del archivo PDF
texto = extraer_texto_pdf(ruta_pdf)

# 2 Detectamos las secciones del texto
secciones = detectar_secciones(texto)

# 3 Creamos la carpeta de salida donde se guardan los archivos
carpeta_salida = "../output/tiende tu cama"

# 4 Separamos el documento
archivos = separar_documentos(
    secciones,
    carpeta_salida
)

# 5 Mostramos el resultado del proceso
print("=" * 60)
print("FASE 4 - SEPARACIÓN DEL DOCUMENTO")
print("=" * 60)

print(f"Secciones detectadas: {len(secciones)}")
print(f"Archivos creados: {len(archivos)}")

print()

# Iteramos el archivo
for archivo in archivos:
    print(f"✓ {archivo}")