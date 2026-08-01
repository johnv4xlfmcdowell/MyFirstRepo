import csv

with open("sepa_data/comercio_12/comercio.csv", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)