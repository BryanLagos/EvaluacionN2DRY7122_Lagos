import requests

# Configura el token de API de MapQuest
token = "eMP1SchjJKqg9klXZGzXnECSyKRLVwNF"

def medir_distancia(origen, destino):
    url = f"http://www.mapquestapi.com/directions/v2/route?key={token}&from={origen}&to={destino}&unit=k"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        distancia = round(data["route"]["distance"], 2)  # Redondear la distancia a dos decimales
        duracion = data["route"]["formattedTime"]  # Nueva línea para obtener la duración del viaje
        narrativa = data["route"]["legs"][0]["maneuvers"]
        return distancia, duracion, narrativa
    else:
        print("Error al obtener la distancia.")
        return None, None, None

# Solicitar la "Ciudad de Origen" al usuario
origen = input("Ingrese la Ciudad de Origen: ")

# Verificar si el usuario quiere salir
if origen.lower() == "q":
    print("Programa finalizado.")
else:
    # Solicitar la "Ciudad de Destino" al usuario
    destino = input("Ingrese la Ciudad de Destino: ")

    # Verificar si el usuario quiere salir
    if destino.lower() == "q":
        print("Programa finalizado.")
    else:
        # Llamada a la función para medir la distancia entre las ciudades proporcionadas
        distancia_km, duracion, narrativa = medir_distancia(origen, destino)

        if distancia_km is not None and duracion is not None and narrativa is not None:
            distancia_km = "{:.2f}".format(distancia_km)  # Formatear la distancia a dos decimales
            print(f"La distancia entre {origen} y {destino} es de {distancia_km} km.")
            print(f"La duración del viaje es de {duracion}.")

            print("Narrativa del viaje:")
            for i, step in enumerate(narrativa, 1):
                print(f"Paso {i}: {step['narrative']}")
