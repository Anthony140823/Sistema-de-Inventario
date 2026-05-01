# Modulo mostrar_inventario
def mostrar_inventario(inventario):
    print("Inventario del almacén:")
    # Preguntamos si la lista está vacía
    if (not inventario):
        print("\n¡Inventario VACÍO! agrega productos")
    else:
        '''
        Recorremos la lista y
        Extraemos los datos de los productos
        '''
        for contador, producto in enumerate(inventario):
            print(f'Id: {producto.get("id")}, Nombre: {producto.get("nombre")}, Precio: {producto.get("precio")}, Cantidad: {producto.get("cantidad")}')