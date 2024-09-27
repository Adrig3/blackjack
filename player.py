from functions import draw_card
from dealer import dealer_gameplay

valor_player = 0

def player_choice():
    global valor_player
    next_move = input("1 = HIT\n 2 = STAND: ")

    if next_move == "1":
        nueva_carta = draw_card()
        valor_player = valor_player + nueva_carta
        print("Has sacado un",nueva_carta)
        player_gameplay()
    
    elif next_move == "2":
        print("Te has plantado con",valor_player)
        dealer_gameplay(valor_player)

def check_valor_player():
    global valor_player
    if valor_player == 21:
        print("¡Has ganado!")
        
    elif valor_player > 21:
        print("Has perdido.")

    elif valor_player < 21:
        print("¿Quieres seguir?")
        player_choice()

def player_gameplay():
    global valor_player
    print("Tienes",valor_player,"puntos.")
    check_valor_player()

def player_start():
    global valor_player
    carta1 = draw_card()
    carta2 = draw_card()
    valor_player = carta1 + carta2

    print("Tus cartas iniciales son:",carta1,"y",carta2)
    print("Tienes",valor_player,"puntos.")
    check_valor_player()
