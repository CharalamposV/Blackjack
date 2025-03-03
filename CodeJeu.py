from random import *
import tkinter as tk
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
