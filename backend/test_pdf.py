# Importamos la funcion extraer_texto del archivo pdf_extractor.py
from app.pdf_extractor import extraer_texto

# Le indicamos la ruta de donde trae el PDF
ruta_pdf = "../tests/pdfs/Tiende_tu_cama_William_H_McRaven.pdf"

# Extraemos el texto del PDF
texto = extraer_texto(ruta_pdf)


print(texto)