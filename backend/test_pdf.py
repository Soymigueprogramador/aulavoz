# Importamos la funcion extraer_texto del archivo pdf_extractor.py
from app.pdf_extractor import extraer_texto

# Le indicamos la ruta de donde trae el PDF
ruta_pdf = "../tests/pdfs/Guía de Ejercicios 1 [maxiprograma.com].pdf"

# Extraemos el texto del PDF
texto = extraer_texto(ruta_pdf)


print(texto)