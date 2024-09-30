import random

options = ["O","X","7"] * 5


def slot_pull():
    symbol = random.choice(options)
    return symbol


def slot_play():
    symbol1 = slot_pull()
    symbol2 = slot_pull()
    symbol3 = slot_pull()

    print("¡Buena suerte!")
    print("--------------")
    print(symbol1,"|",symbol2,"|",symbol3)
    print("--------------")
    if symbol1 == symbol2 == symbol3:
        print("¡Has ganado!")

    else:
        choice = input("Has perdido, ¿quieres probar de nuevo? - SI = 1 | NO = 2: ")
        if choice == "1":
            slot_play()
        else:
            exit