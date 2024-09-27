import random

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11] * 4

def draw_card():
    carta = random.choice(deck)
    deck.remove(carta) 
    return carta

