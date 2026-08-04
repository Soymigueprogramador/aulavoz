import re

from app.pdf_extractor import extraer_texto
from app.section_detector import detectar_secciones


ruta_pdf = "../tests/pdfs/Tiende_tu_cama_William_H_McRaven.pdf"

texto = extraer_texto(ruta_pdf)


print("========== TODAS LAS APARICIONES ==========")


capitulos = [
    "uno",
    "dos",
    "tres",
    "cuatro",
    "cinco",
    "seis",
    "siete",
    "ocho",
    "nueve",
    "diez"
]


for numero in capitulos:

    patron = rf"(?i)capítulo\s+{numero}"

    coincidencias = list(re.finditer(patron, texto))

    print(f"\nCAPÍTULO {numero}: {len(coincidencias)} aparición(es)")

    for coincidencia in coincidencias:

        posicion = coincidencia.start()

        print(f"  posición: {posicion}")
        print(f"  texto: {repr(texto[posicion:posicion + 100])}")


print("\n========== COMIENZO DEL TEXTO ==========")

print(repr(texto[:5000]))


print("\n========== TEXTO ALREDEDOR DEL COMIENZO DEL CAPÍTULO ==========")

posicion = texto.find("cuartel para el entrenamiento básico")

print("Posición:", posicion)

inicio = max(0, posicion - 500)
fin = posicion + 1000

print(repr(texto[inicio:fin]))


print("\n========== BÚSQUEDA POR PÁGINAS ==========")

import fitz

documento = fitz.open(ruta_pdf)

for numero_pagina, pagina in enumerate(documento):

    texto_pagina = pagina.get_text()

    if "cuartel para el entrenamiento básico" in texto_pagina.lower():

        print(f"\nEncontrado en página PDF: {numero_pagina + 1}")

        print(repr(texto_pagina[:2000]))

print("\n========== BÚSQUEDA DE COMIENZOS DE CAPÍTULOS ==========")

frases = [
    "No podrás lograrlo solo",
    "Solo importa el tamaño de tu corazón",
    "La vida no es justa",
    "El fracaso puede fortalecerte",
    "Arriésgate en grande",
    "Enfréntate a los bravucones",
    "Ponte a la altura de las circunstancias",
    "Dale esperanza a la gente",
    "Nunca jamás te des por vencido"
]

for frase in frases:

    encontrado = False

    for numero_pagina, pagina in enumerate(documento):

        texto_pagina = pagina.get_text()

        if frase.lower() in texto_pagina.lower():

            print(f"\n'{frase}' → página PDF: {numero_pagina + 1}")

            print(repr(texto_pagina[:500]))

            encontrado = True
            break

    if not encontrado:

        print(f"\n'{frase}' → NO ENCONTRADO")