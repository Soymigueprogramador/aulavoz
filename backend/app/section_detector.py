# ¿Qué hace?
###
# Por ejemplo si recibe:
#
# Capítulo uno
# Introducción
#
# La programación es...
#
# Capítulo dos
# Variables
#
# Una variable es...
#
# Busca "Capítulo uno", "Capítulo dos", etc.
# y separa el texto que está en cada capítulo
# en una lista de diccionarios.
#
# Ejemplo:
#
# [
#     {
#         "titulo": "Capítulo uno",
#         "contenido": "Introducción..."
#     },
#     {
#         "titulo": "Capítulo dos",
#         "contenido": "Variables..."
#     }
# ]
###
import re


NUMEROS_CAPITULOS = {
    "UNO": 1,
    "DOS": 2,
    "TRES": 3,
    "CUATRO": 4,
    "CINCO": 5,
    "SEIS": 6,
    "SIETE": 7,
    "OCHO": 8,
    "NUEVE": 9,
    "DIEZ": 10,
}


def detectar_secciones(texto):

    patron = re.compile(
        r"(?im)^CAPÍTULO\s+"
        r"(UNO|DOS|TRES|CUATRO|CINCO|SEIS|SIETE|OCHO|NUEVE|DIEZ)"
        r"\.\s*(.+)$"
    )

    coincidencias = list(patron.finditer(texto))

    secciones = []

    for i, coincidencia in enumerate(coincidencias):

        numero_texto = coincidencia.group(1).upper()
        titulo = coincidencia.group(2).strip()

        inicio = coincidencia.end()

        if i + 1 < len(coincidencias):
            fin = coincidencias[i + 1].start()
        else:
            fin = len(texto)

        contenido = texto[inicio:fin].strip()

        secciones.append({
            "numero": NUMEROS_CAPITULOS[numero_texto],
            "titulo": titulo,
            "contenido": contenido,
        })

    return secciones