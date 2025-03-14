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

def win(main_j,main_c):
    result=False
    if len(main_j)==2 and score(main_j)==21:
        result=True
        return result
    elif len(main_j)<len(main_c) and score(main_j)==21:
        result=True
        return result
    elif len(main_c)==2 and score(main_c)==21:
        return result
    elif len(main_c)<len(main_j) and score(main_c)==21:
        return result
    elif score(main_j)>21:
        return result
    elif score(main_c)>21:
        result=True
        return result
    else:
        return

    

def hit():
    global deck
    global main_j
    carte=distrib_cartes(deck,1)
    main_j.append(carte[0])

def stand():
    continue

deck = cartes_deck()
main_j = distrib_carte(deck,2)
main_j = distrib_carte(deck,2)

while win() != True and win()!=False:
    






