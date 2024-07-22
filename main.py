import menu
def menu_prin():
    menu = ["1. Entrar como jefe", "2. Entrar como administrador", "3. Entrar como usuario"]
    for m in menu:
        print(m)


while True:
    print("Bienvenido a Tritech")
    menu_prin()
    opcion = int(input("Elija una opcion: "))
    if opcion == 1:
        menu.entrada_jefe()
    elif opcion ==2:
        menu.entrada_admin()
    elif opcion == 3:
        menu.todo_usuario()
    elif opcion == 4:
        print("Saliendo...")
        break
    else:
        print("Elija una opcion valida")
    