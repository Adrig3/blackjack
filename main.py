from player import player_start

# Le da a elegir al jugador y carga una cosa dependiendo de su opción
def seleccion():

    opcion = input("Escribe opción (1-2): ")

    if opcion == "2":
        print("sample text")

    elif opcion == "1":
        print("¡Juguemos!")
        player_start()

    else:
        print("Opción invalida, seleccione otra otra opción")
        seleccion()

# Le muestra al jugador un menú con opciones
def menu():

    print("Bienvenido al Blackjack, ¿esta es tu primera vez jugando?")
    print("No - 1 \n Si - 2")
    seleccion()




menu()