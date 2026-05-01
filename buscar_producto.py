# Modulo para buscar producto por id
def buscar_producto(inventario, id:int):
    # Variable para determinar si un producto fue encontrado
    # caso contrario se imprime un mensaje
    encontrado = False

    # Recorremos la lista de los produtos
    for producto in inventario:
        # preguntamos si el id del producto está dentro de la lista
        if (id == producto["id"]):
            print(f'Id: {producto.get("id")}, Nombre: {producto.get("nombre")}, Precio: {producto.get("precio")}, Cantidad: {producto.get("cantidad")}')
            encontrado = True
            break
    if (encontrado == False):
        print("Producto no encontrado")