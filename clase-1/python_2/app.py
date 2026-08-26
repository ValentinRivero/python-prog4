import csv
import json
from validar_productos import validar_datos

def calcular_promedio_precio(lista):
    if not lista:
        return 0
    total_precio = sum(p['precio'] for p in lista)
    return total_precio / len(lista)

productos_desde_csv = []

try:
    with open('datos.csv', mode='r', encoding='utf-8') as archivo_csv:
        lector_diccionario = csv.DictReader(archivo_csv)
        for fila in lector_diccionario:
            fila['id'] = int(fila['id'])
            fila['precio'] = int(fila['precio'])
            fila['stock'] = int(fila['stock'])
            productos_desde_csv.append(fila)
except FileNotFoundError:
    print("Error: El archivo 'datos.csv' no se encontró.")

if productos_desde_csv:
    datos_json = json.dumps(productos_desde_csv, indent=4)
    with open('salida.json', 'w') as archivo_salida:
        archivo_salida.write(datos_json)
        
    print("\nArchivo 'salida.json' creado con éxito.")
    print("\n--- Ejecutando el validador modular ---")
    
    datos_validados = validar_datos('salida.json')
    if datos_validados:
        print("Datos validados correctamente:", datos_validados)