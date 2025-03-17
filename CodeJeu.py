from random import *
from tkinter import messagebox
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
            for i in range(2,11):
                if str(i) in carte:
                    score+=i
                else:
                    continue
    return score

def distrib_cartes(deck,nb_cartes): #distribuer le nombre de cartes demandées
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



def jouer_croupier(): # selon la règle de la banque tire a 16 et reste a 17
    global main_c
    while score(main_c) < 17:
        main_c.append(deck.pop())
    if score(main_c) > 21:
        messagebox.showinfo("Le croupier a dépassé 21 ")  #d'apres docspython.org
    elif score(main_j) > score(main_c):
        messagebox.showinfo("Vous avez gagné !")
    elif score(main_j) < score(main_c):
        messagebox.showinfo("Vous avez perdu, le croupier a une meilleure main.")
    else:
        messagebox.showinfo("Vous avez fait jeux égales !")
        
def abandon():
    global main_j
    for i in range(3):
        main_j.append(10)    

# Creation d'une nouvelle partie
def nouveu_deck():
    global deck
    deck=nouveau_deck()
    return 
    
def nouvelle_partie():
    global main_j
    global main_c
    nouveau_deck()
    main_j.clear()
    main_c.clear()
    main_j = distrib_cartes(deck,2)
    main_c = distrib_cartes(deck,2)
    
    
deck = cartes_deck()
main_j = distrib_cartes(deck,2)
main_c = distrib_cartes(deck,2)

print("main joueur: ",main_j, "score: ", score(main_j))
print("main joueur: ",main_j[1], "score: ", score(main_c[1]))

while win() != True and win()!=False:
    choix = input("Voulez vous Hit ou Stand ?")
    if choix=="Hit":
        hit()
    jouer_croupier()
    print("score du joueur est de: ",score(main_j), "\n le score du croupier est de: ",score(main_c))


    
    
    








