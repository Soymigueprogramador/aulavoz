import fitz
import pytesseract
from PIL import Image
import io


def extraer_texto_pagina(pagina):
    """
    Extrae el texto de una página PDF.

    Primero intenta extracción normal con PyMuPDF.
    Si solamente encuentra el número de página
    o no encuentra texto útil, utiliza OCR.
    """

    texto = pagina.get_text().strip()

    # Si encontramos texto real, lo utilizamos.
    if texto and not texto.isdigit():
        return texto

    # Si no hay texto útil, hacemos OCR.
    pix = pagina.get_pixmap(dpi=300)

    imagen_bytes = pix.tobytes("png")

    imagen = Image.open(io.BytesIO(imagen_bytes))

    texto_ocr = pytesseract.image_to_string(
        imagen,
        lang="spa"
    )

    return texto_ocr.strip()


def extraer_paginas_pdf(pdf_path):
    """
    Extrae el texto de todas las páginas del PDF
    conservando el número de página.
    """

    doc = fitz.open(pdf_path)

    paginas = []

    for numero, pagina in enumerate(doc, start=1):

        texto = extraer_texto_pagina(pagina)

        paginas.append({
            "pagina": numero,
            "texto": texto,
        })

    doc.close()

    return paginas


def extraer_texto_pdf(pdf_path):
    """
    Mantiene compatibilidad con el extractor anterior.

    Devuelve todo el texto del PDF como un único string.
    """

    paginas = extraer_paginas_pdf(pdf_path)

    textos = [
        pagina["texto"]
        for pagina in paginas
    ]

    return "\n".join(textos)