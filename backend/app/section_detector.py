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
# Busca los capítulos y separa el texto que está
# dentro de cada capítulo en una lista de diccionarios.
#
# Importante:
# Los PDF pueden contener un índice donde aparecen
# los nombres de los capítulos antes del contenido real.
#
# Por eso no debemos tomar automáticamente la primera
# aparición de "Capítulo uno", ya que podría pertenecer
# al índice.
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


def detectar_secciones(texto):
    secciones = []

    patron = (
        r"(?im)^Capítulo\s+"
        r"(uno|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez)"
        r"\s*$"
    )

    coincidencias = list(re.finditer(patron, texto))

    # Por ahora mostramos las coincidencias encontradas
    # para comprobar cómo se comporta el PDF.
    print("========== COINCIDENCIAS ENCONTRADAS ==========")

    for coincidencia in coincidencias:
        print(
            repr(coincidencia.group()),
            "posición:",
            coincidencia.start()
        )

    # Si no encontramos capítulos, devolvemos una lista vacía.
    if not coincidencias:
        return secciones

    # La primera coincidencia puede pertenecer al índice.
    # Por eso buscamos una segunda aparición de "Capítulo uno"
    # para identificar el comienzo real del contenido.
    #
    # En este PDF concreto, sin embargo, el contenido del
    # capítulo uno no contiene un encabezado "Capítulo uno"
    # limpio, por lo que esta lógica todavía debe ajustarse
    # según la estructura real del PDF.

    for i, coincidencia in enumerate(coincidencias):

        titulo = coincidencia.group().strip()

        inicio = coincidencia.end()

        if i + 1 < len(coincidencias):
            fin = coincidencias[i + 1].start()
            contenido = texto[inicio:fin].strip()
        else:
            contenido = texto[inicio:].strip()

        secciones.append({
            "titulo": titulo,
            "contenido": contenido
        })

    return secciones