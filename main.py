''''
        RETO: SISTEMA DE INVENTARIOS

Crear un sistema de inventarios que tenga las siguientes opciones:

Mostrar un menú:
    1. Mostrar inventario
    2. Agregar nuevo producto
    3. Buscar productor por ID
    4. Salir

Detalle de un Producto:
ID          Precio
Nombre      Cantidad
'''

# Modula main.py 
from menu_interactivo import menu_interactivo

inventario = []

# Impresión del Título y el menú
print("*** Sistema de Inventarios (con funciones) ***")
menu_interactivo(inventario)