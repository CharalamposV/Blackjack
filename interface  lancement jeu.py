from random import *
import tkinter as tk
import random
def cartes_deck():
    couleur = ['carreau','coeur','pique','trefle']
    valeur = ['as','2','3','4','5','6','7','8','9','10','valet','dame','roi']
    deck=[]
    for i in couleur:
        for k in valeur:
            deck.append(k+' de '+ i)
        shuffle(deck)
    return deck
print(cartes_deck())


def distribution_cartes():
    tirage_1_joueur=random.choice(cartes_deck)
    deck-= tirage_1_joueur
    tirage_1_croupier=random.choice(cartes_deck)
    deck-=tirage_1_croupier
    tirage_2_joueur=random.choice(cartes_deck)
    deck-=tirage_2_joueur
    tirage_2_croupier=random.choice(cartes_deck)
    deck-=tirage_2_croupier

