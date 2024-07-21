import cargar_guardar as car
def ingreso_admin():
    while True:
        try:
            bibli = car.cargar()
            documento = int(input("Digite su cedula para darle acceso: "))
            if str(documento) in bibli["Administrador"]:
                print("Bienvenido Administrador", bibli["Administrador"][str(documento)]["Nombres"])
                break
            else:
                print("Contraseña incorrecta")
                
        except Exception:
            print("Algo salio mal intenta de nuevo")

#ingreso_admin()
def regis_admin():
    while True:
        try: 
            bibli = car.cargar()
            datos = {}
            documento = int(input("Digite su cedula: "))
            if str(documento) in bibli["Administrador"]:
                print("Ya hay un usuario registrado con ese documento")
            else:
                datos["Nombres"] = str(input("Digite sus nombres: "))
                datos["Apellidos"] = str(input("Digite sus apellidos: "))
                datos["Telefono"] = int(input("Digite su numero de telefono: "))
                bibli["Administrador"][documento] = datos
                car.guardar(bibli)
                print("Felicitaciones su usuario se ha creado satisfactoriamente ")
                print("*******************************************")
                break
        except Exception:
                    print("Porfavor ingrese sus datos bien, algo salio mal")
#regis_admin()

def edit_admin():
    while True:
        try:
            bibli = car.cargar()
            datos = {}
            documento =input("Digite la cedula del admin que desea modificar: ")
            if str(documento) in bibli["Administrador"]:
                datos["Nombres"] = str(input("Digite sus nombres: "))
                datos["Apellidos"] = str(input("Digite sus apellidos: "))
                datos["Telefono"] = int(input("Digite su numero de telefono: "))
                bibli["Administrador"][documento] = datos
                car.guardar(bibli)
                print("Felicitaciones su usuario se ha actualizado satisfactoriamente ")
                print("*******************************************")
                break
            else:
                print("No hay ningun Admin registrado con esa cedula")

        except Exception:
                    print("Porfavor ingrese sus datos bien, algo salio mal")

#edit_admin()