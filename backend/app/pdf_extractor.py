# Importamos fitz
import fitz

# Funcion para extraer el texto de un PDF
def extraer_texto(ruta_pdf):
    # Ruta del archivo PDF
    documento = fitz.open(ruta_pdf)

    # Variable para guardar el texto
    texto = ""

    # Iteramos para sacar el texto de las paginas del PDF
    for pagina in documento:
        texto =pagina.get_text()

    # Cerramos el PDF
    documento.close()

    # Retornamos el texto
    return texto