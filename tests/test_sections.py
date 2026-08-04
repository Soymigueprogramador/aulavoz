import fitz

PDF_PATH = "../tests/pdfs/Tiende_tu_cama_William_H_McRaven.pdf"

doc = fitz.open(PDF_PATH)

for numero_pagina in [6, 7, 11, 12]:

    pagina = doc[numero_pagina - 1]

    print("\n" + "=" * 60)
    print(f"PÁGINA PDF {numero_pagina}")
    print("=" * 60)

    print("Texto extraído:")
    print(repr(pagina.get_text()))

    print("\nCantidad de imágenes:")
    print(len(pagina.get_images(full=True)))