# Importacion de librerias y archivos necesarios
from fastapi import APIRouter, UploadFile, File
import shutil
import os

# Llamamos al enrrutador
router = APIRouter()

# Creamos el endpoint
@router.post("/convertir")

async def convertir_pdf(pdf: UploadFile = File(...)):
    carpeta = "uploads"
    os.makedirs(carpeta, exist_ok=True)

    ruta_pdf = os.path.join(carpeta, pdf.filename)

    with open( ruta_pdf, "wb" ) as buffer:
        shutil.copyfileobj(pdf.file, buffer)

    return {
        "mensaje": "PDF recibido correctamente",
        "archivo": pdf.filename
    }