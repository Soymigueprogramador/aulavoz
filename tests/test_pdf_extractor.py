from app.pdf_extractor import extraer_texto_pagina
import fitz


PDF_PATH = "../tests/pdfs/Tiende_tu_cama_William_H_McRaven.pdf"

PAGINAS_PRUEBA = [6, 7, 11, 12]


doc = fitz.open(PDF_PATH)


for numero_pagina in PAGINAS_PRUEBA:

    print("=" * 60)
    print(f"PÁGINA PDF {numero_pagina}")
    print("=" * 60)

    pagina = doc[numero_pagina - 1]

    texto = extraer_texto_pagina(pagina)

    print(texto)


doc.close()