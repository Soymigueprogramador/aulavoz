import fitz
import pytesseract
from PIL import Image
import io


def extraer_texto_pagina(pagina):
    """
    Extrae el texto de una página PDF.

    Primero intenta extraer texto directamente con PyMuPDF.
    Si la página no contiene texto, utiliza OCR con Tesseract.
    """

    # 1. Intentar extracción normal
    texto = pagina.get_text()

    if texto.strip():
        return texto

    # 2. Si no hay texto, utilizar OCR
    pix = pagina.get_pixmap(dpi=300)

    imagen_bytes = pix.tobytes("png")

    imagen = Image.open(io.BytesIO(imagen_bytes))

    texto_ocr = pytesseract.image_to_string(
        imagen,
        lang="spa"
    )

    return texto_ocr


def extraer_texto_pdf(pdf_path):
    """
    Extrae el texto completo de un PDF.

    Utiliza extracción normal cuando es posible
    y OCR cuando una página no contiene texto.
    """

    doc = fitz.open(pdf_path)

    textos = []

    for pagina in doc:
        texto = extraer_texto_pagina(pagina)
        textos.append(texto)

    doc.close()

    return "\n".join(textos)