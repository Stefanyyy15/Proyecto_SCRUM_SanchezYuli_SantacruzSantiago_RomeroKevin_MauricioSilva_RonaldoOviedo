import json

# Datos globales
data = {}  # Productos disponibles
carrito = {}  # Productos en el carrito
RUTA_ARCHIVO = "productos.json"  
RUTA_FACTURAS = "facturas.json"  

def guardar_datos():
    """Guarda los datos de productos en un archivo JSON."""
    global data, RUTA_ARCHIVO
    try:
        contenido = json.dumps(data, indent=4)
        with open(RUTA_ARCHIVO, "w") as file:
            file.write(contenido)
        print("Datos guardados exitosamente!!")
    except Exception as e:
        print(f"Error al guardar datos: {e}")

def cargar_datos():
    """Carga los datos de productos desde un archivo JSON."""
    global data, RUTA_ARCHIVO
    try:
        with open(RUTA_ARCHIVO, "r") as file:
            data = json.load(file)
        print("Datos cargados exitosamente!!")
    except FileNotFoundError:
        print(f"El archivo '{RUTA_ARCHIVO}' no existe. Se creará uno nuevo.")
        data = {}
    except json.JSONDecodeError as e:
        print(f"Error al cargar datos JSON: {e}. Se creará un nuevo archivo.")
        data = {}
    except Exception as e:
        print(f"Error general al cargar datos: {e}")
        data = {}

def registrar_producto():
    print("****************************************************************************")
    """Registra un nuevo producto o tipo de producto."""
    global data
    while True:
        print("\nOpciones de tipo de producto:")
        opciones = list(data.keys()) + ["nuevo tipo de producto"]
        for i, opcion in enumerate(opciones, 1):
            print(f"{i}. {opcion.capitalize()}")

        seleccion = input("Seleccione el tipo de producto (número): ")

        if seleccion.isdigit():
            seleccion = int(seleccion)
            if 1 <= seleccion <= len(opciones):
                if seleccion == len(opciones):
                    tipo_producto = input("Ingrese el nuevo tipo de producto: ").lower()
                    if tipo_producto not in data:
                        data[tipo_producto] = []
                else:
                    tipo_producto = opciones[seleccion - 1]
                
                producto = {}
                producto["marca"] = input("Ingrese la marca del producto: ")
                producto["referencia"] = input("Ingrese la referencia del producto: ")
                try:
                    producto["precio"] = int(input("Ingrese el precio del producto: "))
                except ValueError:
                    print("Ingrese un valor válido para el precio del producto")
                    continue
                try:
                    producto["cantidad"] = int(input("Ingrese la cantidad: "))
                except ValueError:
                    print("Ingrese un valor correcto para la cantidad")
                    continue

                data[tipo_producto].append(producto)
                guardar_datos()
                break
        else:
            print("Selección no válida. Intente nuevamente.")

def mostrar_productos():
    print("*******************************************************************************")
    """Muestra todos los productos disponibles."""
    global data
    for tipo_producto, productos in data.items():
        print(f"Tipo de producto: {tipo_producto}")
        for producto in productos:
            print(f"  Referencia: {producto['referencia']}")
            print(f"  Precio: {producto['precio']}")
            print(f"  Cantidad: {producto['cantidad']}")

def eliminar_producto():
    print("***************************************************************************")
    """Elimina un producto específico por referencia."""
    global data
    tipo_producto = input("Ingrese el tipo de producto: ")
    if tipo_producto in data:
        referencia = input("Ingrese la referencia del producto a eliminar: ")
        data[tipo_producto] = [producto for producto in data[tipo_producto] if producto["referencia"] != referencia]
        guardar_datos()
    else:
        print("Tipo de producto no encontrado")

def actualizar_producto():
    print("************************************************************************************")
    """Actualiza el precio y/o cantidad de un producto."""
    global data
    tipo_producto = input("Ingrese el tipo de producto: ")
    if tipo_producto in data:
        referencia = input("Ingrese la referencia del producto a actualizar: ")
        for producto in data[tipo_producto]:
            if producto["referencia"] == referencia:
                try:
                    nuevo_precio = int(input("Ingrese el nuevo precio del producto: "))
                    producto["precio"] = nuevo_precio
                except ValueError:
                    print("Ingrese un valor numérico para el precio.")
                    return
                try:
                    cambio_cantidad = int(input("Ingrese la cantidad a sumar (+) o restar (-): "))
                    nueva_cantidad = producto["cantidad"] + cambio_cantidad
                    if nueva_cantidad < 0:
                        print("No se puede tener una cantidad negativa.")
                        return
                    producto["cantidad"] = nueva_cantidad
                except ValueError:
                    print("Ingrese un valor numérico para la cantidad.")
                    return
                guardar_datos()
                return
        print("Referencia no encontrada.")
    else:
        print("Tipo de producto no encontrado.")

def eliminar_tipo_producto():
    print("*******************************************************************************************")
    """Elimina un tipo de producto junto con todos sus productos."""
    global data
    while True:
        print("\nTipos de productos disponibles:")
        opciones = list(data.keys())
        for i, opcion in enumerate(opciones, 1):
            print(f"{i}. {opcion.capitalize()}")

        seleccion = input("Seleccione el tipo de producto a eliminar (número): ")

        if seleccion.isdigit():
            seleccion = int(seleccion)
            if 1 <= seleccion <= len(opciones):
                tipo_producto = opciones[seleccion - 1]
                confirmacion = input(f"¿Está seguro de que desea eliminar el tipo de producto '{tipo_producto}' y todos sus productos? (s/n): ").lower()
                if confirmacion == 's':
                    del data[tipo_producto]
                    guardar_datos()
                    print(f"Tipo de producto '{tipo_producto}' eliminado exitosamente.")
                    break
                else:
                    print("Operación cancelada.")
                    break
        else:
            print("Selección no válida. Intente nuevamente.")

def agregar_al_carrito():
    print("***************************************************************************************")
    """Permite al usuario agregar productos al carrito."""
    global data, carrito
    while True:
        print("\nOpciones de tipo de producto:")
        opciones = list(data.keys())
        for i, opcion in enumerate(opciones, 1):
            print(f"{i}. {opcion.capitalize()}")

        seleccion = input("Seleccione el tipo de producto (número): ")

        if seleccion.isdigit():
            seleccion = int(seleccion)
            if 1 <= seleccion <= len(opciones):
                tipo_producto = opciones[seleccion - 1]
                productos = data[tipo_producto]

                print("\nProductos disponibles:")
                for i, producto in enumerate(productos, 1):
                    print(f"{i}. {producto['referencia']} - {producto['precio']} - Cantidad disponible: {producto['cantidad']}")

                seleccion_producto = input("Seleccione el producto (número): ")

                if seleccion_producto.isdigit():
                    seleccion_producto = int(seleccion_producto)
                    if 1 <= seleccion_producto <= len(productos):
                        producto_seleccionado = productos[seleccion_producto - 1]
                        cantidad = int(input("Ingrese la cantidad a agregar al carrito: "))

                        if cantidad <= producto_seleccionado["cantidad"]:
                            if tipo_producto not in carrito:
                                carrito[tipo_producto] = []

                            producto_en_carrito = next((item for item in carrito[tipo_producto] if item["referencia"] == producto_seleccionado["referencia"]), None)
                            if producto_en_carrito:
                                producto_en_carrito["cantidad"] += cantidad
                            else:
                                carrito[tipo_producto].append({"referencia": producto_seleccionado["referencia"], "precio": producto_seleccionado["precio"], "cantidad": cantidad})

                            print(f"Producto '{producto_seleccionado['referencia']}' agregado al carrito.")
                        else:
                            print("Cantidad no disponible.")
                        break
                    else:
                        print("Selección de producto no válida.")
                else:
                    print("Selección de producto no válida.")
            else:
                print("Selección de tipo de producto no válida.")
        else:
            print("Selección no válida. Intente nuevamente.")

def actualizar_cantidad_carrito():
    print("**************************************************************************************")
    """Actualiza la cantidad de un producto en el carrito."""
    global carrito
    tipo_producto = input("Ingrese el tipo de producto en el carrito: ")
    if tipo_producto in carrito:
        referencia = input("Ingrese la referencia del producto en el carrito: ")
        for producto in carrito[tipo_producto]:
            if producto["referencia"] == referencia:
                try:
                    nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
                    if nueva_cantidad <= 0:
                        carrito[tipo_producto].remove(producto)
                        if not carrito[tipo_producto]:
                            del carrito[tipo_producto]
                    else:
                        producto["cantidad"] = nueva_cantidad
                    print("Cantidad actualizada.")
                except ValueError:
                    print("Ingrese un valor numérico para la cantidad.")
                return
        print("Referencia no encontrada en el carrito.")
    else:
        print("Tipo de producto no encontrado en el carrito.")

def eliminar_del_carrito():
    """Elimina un producto del carrito."""
    global carrito
    tipo_producto = input("Ingrese el tipo de producto en el carrito: ")
    if tipo_producto in carrito:
        referencia = input("Ingrese la referencia del producto a eliminar del carrito: ")
        carrito[tipo_producto] = [producto for producto in carrito[tipo_producto] if producto["referencia"] != referencia]
        if not carrito[tipo_producto]:
            del carrito[tipo_producto]
        print("Producto eliminado del carrito.")
    else:
        print("Tipo de producto no encontrado en el carrito.")

def visualizar_total_carrito():
    print("********************************************************************************")
    """Visualiza el total del carrito."""
    global carrito
    total = sum(producto["precio"] * producto["cantidad"] for productos in carrito.values() for producto in productos)
    print(f"Total del carrito: {total}")

def guardar_factura():
    """Genera y guarda una factura basada en el carrito y actualiza el inventario."""
    global carrito, data, RUTA_FACTURAS
    facturas = []
    try:
        with open(RUTA_FACTURAS, "r") as file:
            facturas = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        pass

    total_factura = sum(producto["precio"] * producto["cantidad"] for productos in carrito.values() for producto in productos)
    factura = {
        "productos": carrito,
        "total": total_factura
    }

    facturas.append(factura)

    try:
        with open(RUTA_FACTURAS, "w") as file:
            json.dump(facturas, file, indent=4)
        print("Factura guardada exitosamente.")
    except Exception as e:
        print(f"Error al guardar la factura: {e}")

    for tipo_producto, productos_carrito in carrito.items():
        for producto_carrito in productos_carrito:
            for producto in data.get(tipo_producto, []):
                if producto["referencia"] == producto_carrito["referencia"]:
                    producto["cantidad"] -= producto_carrito["cantidad"]
                    break
    guardar_datos()
    carrito.clear()  

def consultar_facturas():
    print("*******************************************************************************")
    """Consulta y muestra las facturas anteriores guardadas."""
    global RUTA_FACTURAS
    try:
        with open(RUTA_FACTURAS, "r") as file:
            facturas = json.load(file)
            for i, factura in enumerate(facturas, 1):
                print(f"\nFactura {i}:")
                for tipo_producto, productos in factura["productos"].items():
                    print(f"Tipo de producto: {tipo_producto}")
                    for producto in productos:
                        print(f"  Referencia: {producto['referencia']}")
                        print(f"  Precio: {producto['precio']}")
                        print(f"  Cantidad: {producto['cantidad']}")
                print(f"Total: {factura['total']}")
    except (FileNotFoundError, json.JSONDecodeError):
        print("No hay facturas disponibles.")

def menu_principal():
    """Muestra el menú principal y gestiona las opciones del usuario."""
    cargar_datos()
    print("**************************************************************************************************")
    while True:
        print("\nMenú:")
        print("1. Registrar producto")
        print("2. Mostrar productos")
        print("3. Eliminar producto")
        print("4. Actualizar producto")
        print("5. Eliminar tipo de producto")
        print("6. Agregar al carrito")
        print("7. Actualizar cantidad en carrito")
        print("8. Eliminar del carrito")
        print("9. Visualizar total del carrito")
        print("10. Guardar factura")
        print("11. Consultar facturas anteriores")
        print("12. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            eliminar_producto()
        elif opcion == "4":
            actualizar_producto()
        elif opcion == "5":
            eliminar_tipo_producto()
        elif opcion == "6":
            agregar_al_carrito()
        elif opcion == "7":
            actualizar_cantidad_carrito()
        elif opcion == "8":
            eliminar_del_carrito()
        elif opcion == "9":
            visualizar_total_carrito()
        elif opcion == "10":
            guardar_factura()
        elif opcion == "11":
            consultar_facturas()
        elif opcion == "12":
            break
        else:
            print("Opción no válida")

menu_principal()
