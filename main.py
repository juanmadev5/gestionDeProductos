productos = []

def añadir_producto():
    # Lógica para añadir un producto
    nombre = input("Ingrese el nombre del producto: ")
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            if precio < 0:
                raise ValueError("El precio no puede ser negativo.")
            break
        except ValueError as e:
            print(f"Entrada inválida. Por favor, ingrese un número válido para el precio.")

    while True:
        try:
            cantidad = int(input("Ingrese la cantidad del producto: "))
            if cantidad < 0:
                raise ValueError("La cantidad no puede ser negativa.")
            break
        except ValueError as e:
            print(f"Entrada inválida. Por favor, ingrese un número válido para la cantidad.")
    producto = {
        'nombre': nombre,
        'precio': precio,
        'cantidad': cantidad
    }
    productos.append(producto)
    print(f"Producto {nombre} ha sido añadido.")

def ver_productos():
    # Lógica para ver todos los productos
    if not productos:
        print("No hay productos añadidos")
        return
    print("Lista de productos: ")
    for n, producto in enumerate(productos, start=1):
        print(f"{n}. Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")

def actualizar_producto():
    # Lógica para actualizar un producto
    ver_productos()
    if not productos:
        print("No hay productos para actualizar.")
        return

    while True:
        try:
            prodNum = int(input("Ingrese el número del producto a editar: ")) - 1
            if 0 <= prodNum < len(productos):
                break
            else:
                print("Número de producto inválido. Por favor, intente de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")

    print("Datos actuales del producto:")
    print(f"Nombre: {productos[prodNum]['nombre']}, Precio: {productos[prodNum]['precio']}, Cantidad: {productos[prodNum]['cantidad']}")

    nombre = input("Nuevo nombre del producto (dejar en blanco para no cambiar): ")
    if nombre:
        productos[prodNum]['nombre'] = nombre

    while True:
        precio = input("Nuevo precio del producto (dejar en blanco para no cambiar): ")
        if precio:
            try:
                nuevo_precio = float(precio)
                if nuevo_precio < 0:
                    raise ValueError("El precio no puede ser negativo.")
                productos[prodNum]['precio'] = nuevo_precio
                break
            except ValueError as e:
                print(f"Entrada inválida. Por favor, ingrese un número válido para el precio.")
        else:
            break

    while True:
        cantidad = input("Nueva cantidad del producto (dejar en blanco para no cambiar): ")
        if cantidad:
            try:
                nueva_cantidad = int(cantidad)
                if nueva_cantidad < 0:
                    raise ValueError("La cantidad no puede ser negativa.")
                productos[prodNum]['cantidad'] = nueva_cantidad
                break
            except ValueError as e:
                print(f"Entrada inválida. Por favor, ingrese un número válido para la cantidad.")
        else:
            break

    print("Producto actualizado con éxito.")


def eliminar_producto():
    # Lógica para eliminar un producto
    ver_productos()
    if not productos:
        print("No hay productos para eliminar.")
        return
    
    while True:
        try:
            prodNum = int(input("Ingrese el número del producto a eliminar: ")) - 1
            if 0 <= prodNum < len(productos):
                break
            else:
                print("Número de producto inválido. Por favor, intente de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")

    producto_eliminado = productos.pop(prodNum)
    print(f"Producto '{producto_eliminado['nombre']}' eliminado con éxito.")


def guardar_datos():
    # Lógica para guardar los datos en un archivo
    with open('productos.txt', 'w') as file:
        for producto in productos:
            file.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    print("Datos guardados con éxito en 'productos.txt'.")

def cargar_datos():
    # Lógica para cargar los datos desde un archivo
    global productos
    try:
        with open('productos.txt', 'r') as file:
            productos = []
            for line in file:
                nombre, precio, cantidad = line.strip().split(',')
                productos.append({
                    'nombre': nombre,
                    'precio': float(precio),
                    'cantidad': int(cantidad)
                })
    except FileNotFoundError:
        print("No se encontró el archivo 'productos.txt'. No hay datos para cargar.")
    except ValueError:
        print("Error al procesar los datos en el archivo. Asegúrate de que el formato sea correcto.")

def menu():
    cargar_datos()
    while True:
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        while True:
            opcion = input("Selecciona una opción: ")
            try:
                opcion = int(opcion)
                if opcion in [1,2,3,4,5]:
                    break
                else:
                    print("Por favor, selecciona una opción válida entre 1 y 5.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")

        if opcion == 1:
            añadir_producto()
        elif opcion == 2:
            ver_productos()
        elif opcion == 3:
            actualizar_producto()
        elif opcion == 4:
            eliminar_producto()
        elif opcion == 5:
            guardar_datos()
            break

            
menu()