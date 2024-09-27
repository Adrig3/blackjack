from functions import draw_card

valor_dealer = 0

def check_valor_dealer(valor_player):
    global valor_dealer
    
    if valor_dealer < 16:
        valor_dealer = valor_dealer + draw_card()
        check_valor_dealer(valor_player)

    elif valor_dealer >= 16 and valor_dealer > valor_player and valor_dealer < 22:
        print("El dealer tiene", valor_dealer,"has perdido")

    elif valor_dealer > 21:
        print("El dealer se ha pasado de 21, has ganado.")
    else:
        print("El dealer tiene", valor_dealer, "¡has ganado!")

def dealer_gameplay(valor_player):
    global valor_dealer
    carta1d = draw_card()
    carta2d = draw_card()
    valor_dealer = carta1d + carta2d
    print("El dealer tiene las cartas:", carta1d, "y", carta2d,"y va a seguir robando hasta 17")
    check_valor_dealer(valor_player)
