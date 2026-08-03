import csv
from mi_lista import agregar_a_mi_lista, cargar_mi_lista

def buscar_por_texto(ruta_archivo, palabra_clave):
    resultados = []
    palabra_clave = palabra_clave.upper()
    with open(ruta_archivo, encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo, delimiter="|")
        for fila in lector:
            descripcion = fila.get('productos_descripcion')
            if descripcion is not None:
                descripcion = descripcion.upper()
                palabras = descripcion.split()
                if palabra_clave in palabras:
                    tiene_negacion = "SIN " + palabra_clave in descripcion
                    if not tiene_negacion:
                        resultados.append(fila)
    return resultados

def buscar_por_id(ruta_archivo, id_producto):
    resultados = []
    with open(ruta_archivo, encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo, delimiter="|")
        for fila in lector:
            if fila.get('id_producto') == id_producto:
                resultados.append(fila)
    return resultados

def buscar_producto(ruta_archivo, id_producto=None, palabra_clave=None):
    if id_producto is not None:
        return buscar_por_id(ruta_archivo, id_producto)
    elif palabra_clave is not None:
        return buscar_por_texto(ruta_archivo, palabra_clave)
    else:
        print("Necesitás pasar un id_producto o una palabra_clave")
        return []

encontrados = buscar_producto("sepa_data/comercio_12/productos.csv", id_producto="7790168903833")
print(f"Se encontraron {len(encontrados)} coincidencias")
for p in encontrados[:5]:
    print(f"{p['productos_descripcion']} - ${p['productos_precio_lista']} - sucursal {p['id_sucursal']}")