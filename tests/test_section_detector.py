from app.pdf_extractor import extraer_texto_pdf
from app.section_detector import detectar_secciones


PDF_PATH = "../tests/pdfs/Tiende_tu_cama_William_H_McRaven.pdf"


texto = extraer_texto_pdf(PDF_PATH)

secciones = detectar_secciones(texto)


print("=" * 60)
print("PRUEBA FINAL - ESTRUCTURA DE SECCIONES")
print("=" * 60)

print(f"Cantidad de secciones: {len(secciones)}")
print()


for i, seccion in enumerate(secciones, start=1):

    print("-" * 60)
    print(f"SECCIÓN {i}")
    print("-" * 60)

    print(f"Tipo: {type(seccion)}")
    print(f"Claves: {seccion.keys()}")

    print(f"Capítulo: {seccion['numero']}")
    print(f"Título: {seccion['titulo']}")

    contenido = seccion["contenido"]

    print(f"Tipo de contenido: {type(contenido)}")
    print(f"Cantidad de caracteres: {len(contenido)}")

    print("Primeros 100 caracteres:")
    print(repr(contenido[:100]))

    print()


print("=" * 60)
print("VALIDACIONES")
print("=" * 60)

print(f"¿Hay 10 secciones?: {len(secciones) == 10}")

print(
    f"¿Todas son diccionarios?: "
    f"{all(isinstance(s, dict) for s in secciones)}"
)

print(
    f"¿Todas tienen número?: "
    f"{all('numero' in s for s in secciones)}"
)

print(
    f"¿Todas tienen título?: "
    f"{all('titulo' in s for s in secciones)}"
)

print(
    f"¿Todas tienen contenido?: "
    f"{all('contenido' in s for s in secciones)}"
)

print(
    f"¿Todas tienen contenido real?: "
    f"{all(len(s['contenido'].strip()) > 0 for s in secciones)}"
)