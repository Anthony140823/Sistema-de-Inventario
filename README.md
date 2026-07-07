# 📦 Sistema de Inventarios en Python

Proyecto desarrollado en Python como parte de una serie de retos prácticos para fortalecer los fundamentos del lenguaje mediante la creación de una aplicación modular de gestión de inventario.

La aplicación permite registrar productos, visualizar el inventario y buscar artículos por su identificador, utilizando estructuras de datos nativas de Python y una arquitectura organizada en módulos.

---

# 📌 Descripción

Este proyecto implementa un sistema básico de inventarios que funciona desde la consola. Los productos se almacenan temporalmente en memoria mediante una lista de diccionarios, donde cada elemento representa un producto con su información principal.

El sistema incorpora un menú interactivo para facilitar la navegación entre las distintas funcionalidades y organiza la lógica del programa en módulos independientes para mejorar la legibilidad y el mantenimiento del código.

---

# 🎯 Objetivos del Proyecto

* Practicar la programación modular en Python.
* Utilizar listas y diccionarios para almacenar información.
* Implementar operaciones básicas sobre un inventario.
* Organizar el código mediante funciones independientes.
* Aplicar estructuras de control para la navegación del sistema.

---

# 🚀 Características

✅ Menú interactivo en consola.

✅ Registro de nuevos productos.

✅ Generación automática de identificadores (ID).

✅ Visualización completa del inventario.

✅ Búsqueda de productos por ID.

✅ Almacenamiento temporal en memoria.

✅ Arquitectura modular con responsabilidades separadas.

---

# 🛠️ Tecnologías Utilizadas

* Python 3
* Funciones
* Modularización
* Listas
* Diccionarios
* Bucles (`while`)
* Estructuras `match-case`
* Entrada y salida por consola

---

# 📂 Estructura del Proyecto

```text
sistema-inventarios/
│
├── main.py
├── menu_interactivo.py
├── agregar_producto.py
├── mostrar_inventario.py
├── buscar_producto.py
└── README.md
```

### Descripción de archivos

| Archivo                 | Responsabilidad                             |
| ----------------------- | ------------------------------------------- |
| `main.py`               | Punto de entrada de la aplicación.          |
| `menu_interactivo.py`   | Gestiona el menú principal y la navegación. |
| `agregar_producto.py`   | Registra nuevos productos en el inventario. |
| `mostrar_inventario.py` | Muestra todos los productos almacenados.    |
| `buscar_producto.py`    | Busca un producto utilizando su ID.         |

---

# ⚙️ Instalación

## Clonar el repositorio

```bash
git clone https://github.com/Anthony140823/Sistema-de-Inventario.git
```

## Acceder al proyecto

```bash
cd Sistema-de-Inventario
```

## Ejecutar

```bash
python main.py
```

---

# ▶️ Uso

Al iniciar la aplicación se mostrará el siguiente menú:

```text
--- MENÚ ---

1. Mostrar inventario
2. Agregar nuevo producto
3. Buscar producto por ID
4. Salir
```

## Agregar un producto

El sistema solicitará:

* Nombre
* Precio
* Cantidad

Cada producto recibirá automáticamente un identificador único.

### Ejemplo

```text
Nombre: Laptop
Precio: 3500
Cantidad: 5

Producto agregado correctamente.
```

---

# 📋 Estructura de los Datos

Cada producto se almacena como un diccionario con la siguiente estructura:

```python
{
    "id": 1,
    "nombre": "Laptop",
    "precio": 3500,
    "cantidad": 5
}
```

Todos los productos se almacenan dentro de una lista que representa el inventario.

---

# 🧠 Conceptos Aplicados

Durante el desarrollo de este proyecto se practicaron los siguientes conceptos:

* Funciones.
* Parámetros.
* Modularización.
* Importación de módulos.
* Listas.
* Diccionarios.
* Recorrido de colecciones.
* Búsqueda secuencial.
* Generación automática de identificadores.
* Menús interactivos.
* Bucles `while`.
* Estructuras `match-case`.
* Organización de proyectos Python.

---

# 📈 Aprendizajes Obtenidos

Este proyecto permitió comprender cómo estructurar una aplicación en múltiples módulos y cómo modelar información utilizando estructuras de datos nativas de Python.

Además, reforzó conceptos relacionados con la búsqueda de información, manipulación de listas y separación de responsabilidades, acercándose a la lógica utilizada en aplicaciones de gestión reales.

---

# 🔮 Mejoras Futuras

Algunas mejoras que podrían implementarse en futuras versiones:

* Editar información de un producto.
* Eliminar productos del inventario.
* Buscar productos por nombre.
* Validar entradas mediante `try-except`.
* Persistencia de datos utilizando archivos JSON.
* Integración con una base de datos SQLite.
* Ordenar productos por nombre, precio o cantidad.
* Implementar Programación Orientada a Objetos.
* Crear una interfaz gráfica con Tkinter.
* Incorporar pruebas unitarias.

---

# 👨‍💻 Autor

**Anthony JeanPaul Reyes Risco**

Desarrollador de software en formación apasionado por la programación y el aprendizaje continuo. Este proyecto forma parte de mi portafolio práctico en Python, donde documento mi progreso mediante el desarrollo de aplicaciones funcionales.

---

# 📄 Licencia

Este proyecto fue desarrollado con fines educativos y forma parte de mi portafolio personal de aprendizaje.
