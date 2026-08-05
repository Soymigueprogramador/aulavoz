import re


CAPITULOS = {
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
    """
    Detecta los capítulos reales del documento.

    El PDF contiene los nombres de los capítulos dos veces:
    1. En el índice.
    2. En el comienzo real de cada capítulo.

    Para cada capítulo utilizamos la última aparición.
    """

    patron = (
        r"CAPÍTULO\s+"
        r"(UNO|DOS|TRES|CUATRO|CINCO|SEIS|SIETE|OCHO|NUEVE|DIEZ)"
    )

    coincidencias = list(
        re.finditer(
            patron,
            texto,
            flags=re.IGNORECASE
        )
    )

    capitulos = {}

    for coincidencia in coincidencias:

        palabra = coincidencia.group(1).upper()

        # Guardamos la última aparición de cada capítulo.
        capitulos[palabra] = {
            "numero": CAPITULOS[palabra],
            "palabra": palabra,
            "inicio": coincidencia.start(),
            "fin_encabezado": coincidencia.end(),
        }

    # Convertimos a lista y ordenamos por posición
    encontrados = sorted(
        capitulos.values(),
        key=lambda x: x["inicio"]
    )

    secciones = []

    for i, capitulo in enumerate(encontrados):

        inicio = capitulo["fin_encabezado"]

        # El contenido termina justo antes del siguiente capítulo.
        if i + 1 < len(encontrados):
            fin = encontrados[i + 1]["inicio"]
        else:
            fin = len(texto)

        contenido = texto[inicio:fin].strip()

        secciones.append({
            "numero": capitulo["numero"],
            "titulo": f"CAPÍTULO {capitulo['palabra']}",
            "contenido": contenido,
        })

    return secciones