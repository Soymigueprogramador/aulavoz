from app.pdf_extractor import extraer_paginas_pdf


PDF_PATH = "../tests/pdfs/Tiende_tu_cama_William_H_McRaven.pdf"


paginas = extraer_paginas_pdf(PDF_PATH)


PAGINAS_PRUEBA = [3, 6, 7, 11, 12, 17]


for numero_pagina in PAGINAS_PRUEBA:

    pagina = paginas[numero_pagina - 1]

    print("=" * 60)
    print(f"PÁGINA PDF {pagina['pagina']}")
    print("=" * 60)

    print(pagina["texto"][:1000])