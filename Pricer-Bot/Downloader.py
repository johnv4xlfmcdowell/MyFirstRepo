import requests
import os
import zipfile

url = "https://datos.produccion.gob.ar/dataset/6f47ec76-d1ce-4e34-a7e1-621fe9b1d0b5/resource/91bc072a-4726-44a1-85ec-4a8467aad27e/download/sepa_viernes.zip"

if not os.path.exists("sepa_viernes.zip"):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        with open("sepa_viernes.zip", "wb") as archivo:
            archivo.write(respuesta.content)
        print("Descarga completa")
    else:
        print(f"Error {respuesta.status_code}")
else:
    print("El archivo ya existe, no hace falta descargarlo de nuevo")

if not os.path.exists("sepa_data"):
    with zipfile.ZipFile("sepa_viernes.zip", "r") as zip_ref:
        print(zip_ref.namelist())
        zip_ref.extractall("sepa_data")
else:
    print("Ya estaba descomprimido")

ruta_interna = "sepa_data/2026-07-31/sepa_1_comercio-sepa-12_2026-07-31_09-05-10.zip"

if not os.path.exists("sepa_data/comercio_12"):
    with zipfile.ZipFile(ruta_interna, "r") as zip_ref:
        print(zip_ref.namelist())
        zip_ref.extractall("sepa_data/comercio_12")
else:
    print("Ese comercio ya estaba descomprimido")