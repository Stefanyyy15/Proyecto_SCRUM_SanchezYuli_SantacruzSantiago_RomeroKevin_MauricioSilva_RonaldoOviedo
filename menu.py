import admin
import registrar_usuario
import facturas

def menu_jefe():
    menu = ["1. Registrar Administrador", "2. Registrar Usuario", "3. Modificar Administrador", "4. Modificar Ususario", "5. Eliminar Administrador", "6. Eliminar usuario", "7. Salir" ]
    for m in menu:
        print(m)



def entrada_jefe():
    contraseña = input("ingrese su contraseña: ")
    if contraseña == "jefe":
        print("Bienvenido jefe")
        while True:
            print("Seleccione una opcion")
            menu_jefe()
            num = int(input("Digite un numero: "))
            if num == 1:
                admin.regis_admin()
            elif num ==2:
                registrar_usuario.usuario()
            elif num ==3:
                admin.edit_admin()
            elif num ==4:
                registrar_usuario.edit_usuarios()
            elif num ==5:
                admin.eliminar_admin()
            elif num ==6:
                admin.eliminar_usuario()
            elif num ==7:
                print("Saliendo...")
                break
            else:
                print("Digite una opcion valida")

#entrada_jefe()


def menu_admin():
    menu = ["1. Registrar ususario", "2. Modificar Usuario", "3. Modificar Administrador", "4. Registrar productos", "5. Eliminar electrodomestico","6. Eleminar referencia" , "7. Actualizar producto", "8. Consultar facturas", "9. eliminar usuario", "10. Salir"]
    for m in menu:
        print(m)

def entrada_admin():
    admin.ingreso_admin()
    while True:
        menu_admin()
        op = int(input("Seleccione una opcion: ")) 
        if op == 1:
            registrar_usuario.usuario()
        elif op == 2:
            registrar_usuario.edit_usuarios()
        elif op == 3:
            admin.edit_admin()
        elif op == 4:
            facturas.registrar_producto()
        elif op == 5:
            facturas.eliminar_tipo_producto()
        elif op == 6:
            facturas.eliminar_producto()
        elif op == 7:
            facturas.actualizar_producto()
        elif op == 8:
            facturas.consultar_facturas()
        elif op == 9:
            admin.eliminar_usuario()
        elif op == 10:
            print("Saliedo...")
            break
        else:
            print("Elija una opcion valida")
#entrada_admin()

def menu_usuario():
    menu = ["1. Registrar Usuario", "2. Iniciar sesion", "3. Salir"]
    for m in menu:
        print(m)






def menu_usuario2():
    menu = ["1. Agregar al carrito", "2. Actualizar cantidad en carrito", "3. Eliminar del carrito", "4. Visualizar total del carrito", "5. Guardar factura", "6. Salir"]
    for m in menu:
        print(m)

def entrada_usuario():
    while True:
        menu_usuario2()
        opci = int(input("Elija una opcion: "))
        if opci == 1:
            facturas.agregar_al_carrito()
        elif opci == 2:
            facturas.actualizar_cantidad_carrito()
        elif opci == 3:
            facturas.eliminar_del_carrito()
        elif opci == 4:
            facturas.visualizar_total_carrito()
        elif opci ==5:
            facturas.guardar_factura()
        elif opci ==6:
            print("Saliendo...")
            break
        else:
            print("Elija una opcion valida")

def todo_usuario():
    while True:
        menu_usuario()
        opc = int(input("Elija una opcion: "))
        if opc == 1:
            registrar_usuario.usuario()
        elif opc == 2:
            registrar_usuario.ingreso_usuario()
        elif opc ==3:
            print("Saliendo...")
            break
        else:
            print("Elija una opcion valida")

