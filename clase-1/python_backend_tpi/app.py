import csv


productos = [
     {"nombre": "Laptop", "precio": 1200, "stock": 15},
     {"nombre": "Mouse", "precio": 25, "stock": 5},
     {"nombre": "Teclado", "precio": 75, "stock": 25},
     {"nombre": "Monitor", "precio": 300, "stock": 8}
]


# productos_bajo_stock = [] # Se crea un array vacio para guardar los productos que después vayamos a indicar como de "bajo stock"
# for producto in productos: # Se itera uno a uno los elementos del array productos
#     print(f"Producto: {producto['nombre']}, Precio: ${producto['precio']}") # Se muestra en pantalla los detalles del producto que está iterando
#     if producto['stock'] < 10: # Se comprueba si el stock del producto es menor a 10
#         productos_bajo_stock.append(producto) # Si el valor de stock es menor a 10, se agrega el producto al array de productos_bajo_stock

# print("\nProductos con bajo stock:") # Imprime en consola un salto de linea y "Productos con bajo stock:"
# print(productos_bajo_stock) # Imprime la lista final de los productos que tienen poco stock


# def calcular_promedio_precio(lista): #Se define una nueva función que recibe como parametro algo que guardará en una variable "lista"
#     if not lista: #Comprueba si la lista que le llega a la función está vacía
#         return 0 #Si la lista está vacía la función devuelve el valor 0
#     total_precio = sum(p['precio'] for p in lista) #En caso de que no esté vacía, suma los precios de cada elemento en la lista de productos
#     return total_precio / len(lista)    #La función devuelve el resultado de la suma de todos los precios dividido la cantidad de elementos
#                                         #en la lista, es decir, el promedio de todos los precios

# precio_promedio = calcular_promedio_precio(productos)   #Se crea una nueva variable a la que se le asigna el valor que devuelva la función
#                                                         #antes creada tras ejecutarse pasandole como parametro la lista "productos"
# print(f"\nEl precio promedio de los productos es: ${precio_promedio:.2f}")  #Imprime por pantalla un texto que explica el número que se va
#                                                                             #a mostrar, y al ser un float, sed limita sus valores decimales a 2

productos_desde_csv = []

with open('datos.csv', mode='r', encoding='utf-8') as archivo_csv: #archivo_csv es un puntero que apunta al archivo
    lector_diccionario = csv.DictReader(archivo_csv)
    for fila in lector_diccionario:
        fila['id'] = int(fila['id'])
        fila['precio'] = int(fila['precio'])
        fila['stock'] = int(fila['stock'])

        productos_desde_csv.append(fila)

print("\nLista de productos desde el archivo CSV:")
#print(productos_desde_csv)

for x in productos_desde_csv:
    print(f"Producto: {x['nombre']}, ID: {x['id']} , Precio: ${x['precio']}, Stock: {x['stock']}")