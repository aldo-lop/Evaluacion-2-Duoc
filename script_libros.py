import random
import requests

# URL de la API de pruebas
url = "http://postman-echo.com/post"

autores_base = [
    "Aldo Lopez",
    "Carlos Gomez",
    "Paola Fuentes",
    "Juan Soto",
    "Madelein Orellana",
]
titulos_base = [
    "Redes Inalambricas",
    "Seguridad Informatica",
    "Python para DevOps",
    "Cloud Computing Basico",
    "Arquitectura de Redes",
]

print("=== INICIANDO CREACION MASIVA DE 50 LIBROS AL AZAR ===")

# Bucle para generar 50 libros adicionales (del ID 8 al 57)
for i in range(8, 58):
  libro_aleatorio = {
      "id": i,
      "titulo": f"{random.choice(titulos_base)} - Edicion {i}",
      "autor": random.choice(autores_base),
      "isbn": str(random.randint(100000000, 999999999)),
  }

  try:
    response = requests.post(url, json=libro_aleatorio)
    if response.status_code in [200, 201]:
      print(
          f"Libro ID {i} creado -> Autor: {libro_aleatorio['autor']} | ISBN:"
          f" {libro_aleatorio['isbn']}"
      )
    else:
      print(f"Error en libro ID {i}: Código {response.status_code}")
  except Exception as e:
    print(f"Fallo de conexión: {e}")

print("\n=== PROCESO DE CREACIÓN FINALIZADO ===")

# Listar la totalidad de los libros creados
print("\n=== LISTANDO LA TOTALIDAD DEL CATÁLOGO ===")
try:
  response_list = requests.get("http://postman-echo.com/get")
  if response_list.status_code == 200:
    print("Catálogo listado con éxito:")
    print(response_list.json())
  else:
    print(f"No se pudo listar. Código: {response_list.status_code}")
except Exception as e:
  print(f"Error al listar: {e}")