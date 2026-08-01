import requests

lat = -37.19   # reemplazá con tu latitud real
lng = -56.88   # reemplazá con tu longitud real

url = "https://d3e6htiiul5ek9.cloudfront.net/prod/sucursales"
params = {"lat": lat, "lng": lng, "limit": 10}

respuesta = requests.get(url, params=params)
print(respuesta.status_code)
print(respuesta.json())