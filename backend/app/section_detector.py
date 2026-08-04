import re


# Detecta capítulos dentro de un texto
def detectar_secciones(texto):
    secciones = []

    # Detecta:
    # CAPÍTULO 1
    # CAPÍTULO UNO
    # CAPITULO 1
    # CAPITULO UNO
    patron = (
        r"(?im)^CAP[ÍI]TULO\s+"
        r"(?:\d+|UNO|DOS|TRES|CUATRO|CINCO|SEIS|SIETE|OCHO|NUEVE|DIEZ)"
        r"\s*$"
    )

    coincidencias = list(re.finditer(patron, texto))

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