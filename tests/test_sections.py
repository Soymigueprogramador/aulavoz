import fitz
import pytesseract
from PIL import Image
import io


PDF_PATH = "../tests/pdfs/Tiende_tu_cama_William_H_McRaven.pdf"


doc = fitz.open(PDF_PATH)

# Página PDF 6
pagina = doc[5]

print("=" * 60)
print("PÁGINA PDF 6")
print("=" * 60)

# Renderizamos la página como imagen
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