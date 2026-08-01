import csv

def buscar_producto(ruta_archivo, palabra_clave):
    resultados = []
    with open(ruta_archivo, encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo, delimiter="|")
        for fila in lector:
            if fila.get('productos_descripcion') is not None:
                if palabra_clave.upper() in fila['productos_descripcion'].upper():
                    resultados.append(fila)
    return resultados

encontrados = buscar_producto("sepa_data/comercio_12/productos.csv", "azucar")
print(f"Se encontraron {len(encontrados)} coincidencias")
for p in encontrados[:5]:
    print(f"{p['productos_descripcion']} - ${p['productos_precio_lista']} - sucursal {p['id_sucursal']}")