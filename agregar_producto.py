# Modulo agregar_producto.py

# Función para agregar un nuevo producto:
def agregar_producto(inventario, nombre:str, precio:float, cantidad:int):
    #el id del produto incia en uno y se incrementa automáticamente:
    id = 1
    # Incializamos el diccionario que alvergará los datos del producto
    producto = {
        "id": id,
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    # Agregamos el producto a la lista de inventario
    inventario.append(producto)
    id += 1
    print("\nProducto agregado correctamente")