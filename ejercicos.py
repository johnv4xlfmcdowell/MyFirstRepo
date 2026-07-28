# dejo los ejercicios corregidos, quiero que me des una devolucion como lo estas haciendo y luego sigamos con nuestra ruta si es posible.
 #Q1 
precios = [890, 750, 920, 680, 810]
sucursales = ["Coto", "Dia", "Carrefour", "Jumbo", "Vea"]


bprice = precios[0]
store = sucursales[0]


def mas_barato(precios, sucursales):
    bprice = precios[0]
    store = sucursales[0]

    for i in range (len(precios)):
        if precios[i] <= bprice:
            bprice = precios[i]
            store = sucursales[i]
    return bprice, store  

precio, lugar = mas_barato(precios, sucursales)

print(f"el mejor precio esta en {lugar}" )

print(f"el mejor precio es: ${bprice} y esta en {store}")









#Q2
presupuesto = 800
cantidad = 0

for i in range (len(precios)):
    if precios[i] <= presupuesto:
        print(precios[i])
        cantidad = cantidad + 1

print (f"solo {cantidad} entran en el presupuesto") 



#Q3 
ofertas = []

for i in range (len(precios)):
    if precios[i] <= presupuesto:
        ofertas.append(precios[i])
for i in range(len(ofertas)):
    print(f"{ofertas[i]}")


#Q4 
i=0
while i < len(precios) :
    if precios[i] <= 800:
        print(f"la oferta es ${precios[i]} y esta en la sucursal {sucursales[i]}")
        encontrado = True
        break
    i = i+1
if not encontrado:
    print("no se encontro oferta")


#dia 2


#Q1
productos = [
    {"nombre": "leche", "precio": 890, "sucursal": "Coto"},
    {"nombre": "leche", "precio": 750, "sucursal": "Dia"},
    {"nombre": "leche", "precio": 680, "sucursal": "Jumbo"},
]

bprice = productos[0]['precio']
resultado = productos[0]

def mas_barato(productos):
    bprice = productos[0]['precio']
    resultado = productos[0]
    for i in range(len(productos)):
        if productos[i]['precio'] <= bprice:
            bprice = productos[i]['precio']
            resultado = productos[i]
    return resultado

resultado = mas_barato(productos)
print(f"el producto mas barato es {resultado['nombre']} y esta en {resultado['sucursal']}: ${resultado['precio']}")
# ahora esta mejor? siento que sigo teniendo un par de errores


