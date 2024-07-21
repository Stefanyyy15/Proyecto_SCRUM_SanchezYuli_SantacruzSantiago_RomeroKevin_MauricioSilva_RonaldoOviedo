import json
ruta = "usuarios.json"

def guardar(datos):
    with open(ruta, "w") as file:
        json.dump(datos, file, indent=4)
        print("Sus datos se han guardao exitosamente")
        print("*******************************************")

def cargar():
    try:
        with open(ruta, "r") as leer:
            datos= json.load(leer)
            return datos
    except Exception:
        print("Error al guardar los datos")
        return {"Usuarios":{}}