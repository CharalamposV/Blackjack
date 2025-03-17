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

def score(carte): #compter le score que donne les cartes en main
    score = 0
    for i in carte:
        if i[0] in ['v','d','r']:
            score += 10
        elif i[0] == 'a':
            if score+11 <= 21:
                score +=11
            else:
                score +=1
        else:
            score += int(i[0]+i[1])    
    return score

def distrib_cartes(deck,nb_cartes): #distribuer le nomvre de carte demandé
    main = []
    for i in range(nb_cartes):
        carte = randint(0, len(deck)-1)
        main.append(deck.pop(deck[carte]))
    return main

def hit():
    global deck
    global main_j
    carte=distrib_cartes(deck,1)
    main_j.append(carte[0])

def stand():
    continue

deck = cartes_deck()
main_j = distrib_cartes(deck,2)
main_j = distrib_cartes(deck,2)

while win() != True and win()!=False:
    continue



def jouer_croupier():
    global main_c
    while score(main_c) < 17:
        main_c.append(deck.pop())
    if score(main_c) > 21:
        messagebox.showinfo("Gagné", "Le croupier a dépassé 21. Vous avez gagné !")  #d'apres docspython.org
    elif score(main_j) > score(main_c):
        messagebox.showinfo("Vous avez gagné !")
    elif score(main_j) < score(main_c):
        messagebox.showinfo("Vous avez perdu, le croupier a une meilleure main.")
    else:
        messagebox.showinfo("Vous avez fait jeux égales !")





