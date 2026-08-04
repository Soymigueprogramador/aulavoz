from app.section_detector import detectar_secciones


texto = """
CAPÍTULO UNO

Empieza tu día con una tarea cumplida.

Si quieres cambiar al mundo,
empieza por tender tu cama.

CAPÍTULO DOS

No podrás lograrlo solo.

Si quieres cambiar al mundo...,
encuentra a alguien que te ayude a remar.
"""


secciones = detectar_secciones(texto)


print(f"Secciones encontradas: {len(secciones)}")
print()


for seccion in secciones:
    print("=" * 50)
    print(seccion["titulo"])
    print("=" * 50)
    print(seccion["contenido"])
    print()