import cargar_guardar as car
import menu
def ingreso_usuario():
        try:
            bibli = car.cargar()
            documento = int(input("Digite su cedula: "))
            if str(documento) in bibli["Usuarios"]:
                print("Bienvenido Usuario", bibli["Usuarios"][str(documento)]["Nombres"])
                menu.entrada_usuario()
            else:
                print("Contraseña incorrecta")
        except Exception:
            print("Algo salio mal intenta de nuevo")



#ingreso_usuario()


def usuario():
    try:
        bibli = car.cargar()
        datos = {}
        documento = int(input("Digite su cedula "))
        if str(documento) in bibli["Usuarios"]:
            print("Ya hay un usuario registrado con ese documento")
        else:
            datos["Nombres"] = str(input("Digite sus nombres "))
            datos["Apellidos"] = str(input("Digite sus apellidos "))
            datos["Telefono"] = int(input("Digite su numero de telefono "))
            bibli["Usuarios"][documento] = datos
            car.guardar(bibli)
            print("Felicitaciones su usuario se ha creado satisfactoriamente ")
            print("*******************************************")
    except Exception:
        print("Coloca bien los datos!!")

#usuario()

def edit_usuarios():
    bibli = car.cargar()
    documento = input("Digite la cédula del usuario que quieres editar: ")
    
    if documento in bibli["Usuarios"]:
        usuario = bibli["Usuarios"][documento]
        nombres = input("Digite sus nombres: ")
        apellidos = input("Digite sus apellidos: ")
        telefono = input("Digite su número de teléfono: ")    
        usuario["Nombres"] = nombres
        usuario["Apellidos"] = apellidos
        try:
            usuario["Telefono"] = int(telefono)
        except ValueError:
            print("Número de teléfono inválido, se mantiene el anterior.")
        bibli["Usuarios"][documento] = usuario
        car.guardar(bibli)
        print("Felicitaciones, su usuario se ha actualizado.")
        print("*******************************************")
    else:
        print("No hay un usuario registrado con esa cédula.")

#edit_usuarios()



