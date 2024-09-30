from player import player_start
from slot import slot_play

# Le da a elegir al jugador y carga una cosa dependiendo de su opción
def seleccion():

    opcion = input("Escribe opción (1-2-3): ")

    if opcion == "3":
        slot_play()

    elif opcion == "2":
        print("https://en.wikipedia.org/wiki/Blackjack")

    elif opcion == "1":
        print("¡Juguemos!")
        player_start()

    else:
        print("Opción invalida, seleccione otra otra opción")
        seleccion()

# Le muestra al jugador un menú con opciones
def menu():

    print("Bienvenido al Blackjack, ¿esta es tu primera vez jugando?")
    print("No - 1 \n Si - 2 \n Quiero jugar a la tragaperras - 3")
    seleccion()




menu()