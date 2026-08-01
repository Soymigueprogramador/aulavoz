# Importamos la libreria FastAPI
from fastapi import FastAPI

# Variable para inicializar el servidor
app = FastAPI()

# Indicamos la ruta de acceso
@app.get("/")

# Funcion para iniciar el servidor
def inicio():
# Si el servidor esta funcionando mostrara este mensaje
    return {
        "mensaje": "AulaVoz Backend funcionando"
    }