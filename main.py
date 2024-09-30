productos = []

def añadir_producto():
    # Lógica para añadir un producto
    pass

def ver_productos():
    # Lógica para ver todos los productos
    pass

def actualizar_producto():
    # Lógica para actualizar un producto
    pass

def eliminar_producto():
    # Lógica para eliminar un producto
    pass

def guardar_datos():
    # Lógica para guardar los datos en un archivo
    pass

def cargar_datos():
    # Lógica para cargar los datos desde un archivo
    pass

def menu():
    while True:
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, selecciona una opción válida.")