import admin
import registrar_usuario


def menu_jefe():
    menu = ["1. Registrar Administrador", "2. Registrar Usuario", "3. Modificar Administrador", "4. Modificar Ususario" ]
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
                print("Saliendo...")
                break
            else:
                print("Digite una opcion valida")

#entrada_jefe()


def menu_admin():
    menu = ["1. Registrar ususario", "2. Modificar Usuario", "3. Modificar Administrador", "4. Salir"]
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
            print("Saliedo...")
            break
#entrada_admin()