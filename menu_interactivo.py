# Modulo menu_intercativo

from agregar_producto import agregar_producto

# Función para mostrar el menú:
def menu_interactivo(inventario):
    while True:
        print('''--- MENÚ ---
            1. Mostrar inventario
            2. Agregar nuevo producto
            3. Buscar productor por ID
            4. Salir
        ''')
        opcion = int(input("Proporciona una opción (1-4): "))

        match opcion:
            case 2:
                # Pedimos al usuario que ingrese los datos del producto
                nombre = input("Nombre: ")
                precio = float(input("Precio: "))
                cantidad = int(input("Cantidad: "))

                # Llamamos a la función agregar producto
                agregar_producto(inventario, nombre, precio, cantidad)
            case 4:
                print("Saliendo del sistema... ¡Adiós!")
                break
            case _:
                print("Opción no válida")