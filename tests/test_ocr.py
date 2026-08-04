import fitz
import pytesseract
from PIL import Image
import io


PDF_PATH = "../tests/pdfs/Tiende_tu_cama_William_H_McRaven.pdf"

# Páginas del PDF que queremos probar
PAGINAS_PRUEBA = [6, 7, 11, 12]


doc = fitz.open(PDF_PATH)


for numero_pagina in PAGINAS_PRUEBA:

    print("=" * 60)
    print(f"PÁGINA PDF {numero_pagina}")
    print("=" * 60)

    # PyMuPDF utiliza índices desde 0
    pagina = doc[numero_pagina - 1]

    # Convertimos la página PDF en imagen
    pix = pagina.get_pixmap(dpi=300)

    # Convertimos la imagen de PyMuPDF a bytes PNG
    imagen_bytes = pix.tobytes("png")

    # Abrimos la imagen con Pillow
    imagen = Image.open(io.BytesIO(imagen_bytes))

    print("Imagen creada correctamente.")
    print(f"Tamaño: {imagen.size}")

    # OCR en español
    texto = pytesseract.image_to_string(
        imagen,
        lang="spa"
    )

    print("\n========== TEXTO OCR ==========\n")
    print(texto)


doc.close()