# Modulo agregar_producto.py

# Función para agregar un nuevo producto:
def agregar_producto(inventario, nombre:str, precio:float, cantidad:int):
    # calculamos el tamaño de la lista
    # para saber qué número de id le corresponde a cada producto
    tamaño =len(inventario)
    id = tamaño + 1
    
    # Incializamos el diccionario que alvergará los datos del producto
    producto = {
        "id": id,
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    # Agregamos el producto a la lista de inventario
    inventario.append(producto)
    print("\nProducto agregado correctamente")