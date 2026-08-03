import json
import os
from datetime import date

RUTA_MI_LISTA = "mis_productos.json"

def cargar_mi_lista():
    if not os.path.exists(RUTA_MI_LISTA):
        return []
    with open(RUTA_MI_LISTA, encoding="utf-8") as archivo:
        return json.load(archivo)

def guardar_mi_lista(lista):
    with open(RUTA_MI_LISTA, "w", encoding="utf-8") as archivo:
        json.dump(lista, archivo, ensure_ascii=False, indent=2)

def agregar_a_mi_lista(id_producto, nombre):
    lista = cargar_mi_lista()
    for producto in lista:
        if producto["id_producto"] == id_producto:
            print("Ese producto ya está en tu lista")
            return
    nuevo = {
        "id_producto": id_producto,
        "nombre": nombre,
        "agregado": str(date.today())
    }
    lista.append(nuevo)
    guardar_mi_lista(lista)
    print(f"Agregado: {nombre}")