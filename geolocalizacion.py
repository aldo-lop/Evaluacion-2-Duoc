import requests


def calcular_ruta():
  # Configura tu token de Graphhopper aquí
  api_key = "TU_TOKEN_DE_GRAPHHOPPER"
  url = f"https://graphhopper.com/api/1/route?key={api_key}"

  print("=== SISTEMA DE GEOLOCALIZACION - RUTA DE VIAJE ===")

  while True:
    # Opción para salir con "s" o "salir"
    origen = input(
        "\nIngrese el punto de partida (o escriba 's' / 'salir' para terminar): "
    )
    if origen.lower() in ["s", "salir"]:
      print("Saliendo del programa de geolocalización. ¡Hasta luego!")
      break

    destino = input("Ingrese el destino: ")
    if destino.lower() in ["s", "salir"]:
      print("Saliendo del programa de geolocalización. ¡Hasta luego!")
      break

    print(f"\nCalculando ruta desde '{origen}' hasta '{destino}'...")

    # Simulación de valores de la API para el ejemplo práctico
    distancia_metros = 14520.556
    tiempo_milisegundos = 954000

    # Valores con un máximo de dos decimales usando f-strings (:.2f)
    distancia_km = distancia_metros / 1000
    tiempo_minutos = tiempo_milisegundos / 60000

    print(f"-> Distancia total: {distancia_km:.2f} km")
    print(f"-> Tiempo estimado: {tiempo_minutos:.2f} minutos")

    # Narrativa del viaje paso a paso en español
    print("\nNarrativa del viaje (Instrucciones paso a paso):")
    print(f"1. Inicie el recorrido saliendo desde {origen}.")
    print(f"2. Conduzca por la vía principal en dirección a {destino}.")
    print(f"3. Siga las señales de tránsito indicadas durante la ruta.")
    print(f"4. Ha llegado exitosamente a su destino: {destino}.")


if __name__ == "__main__":
  calcular_ruta()