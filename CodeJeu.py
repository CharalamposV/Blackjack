from random import *
from tkinter import messagebox
import tkinter as tk

def cartes_deck(): #fonction de création dun jeu de cartes
    couleur = ['carreau','coeur','pique','trefle']
    valeur = ['as','2','3','4','5','6','7','8','9','10','valet','dame','roi']
    deck=[]
    for i in couleur:
        for k in valeur:
            deck.append(k+' de '+ i)
    shuffle(deck)
    return deck

def win(main_j,main_c,mise): #fonction de conditions de victoire 
    global banque
    result=False
    if len(main_j)==2 and score(main_j)==21:
        result=True
        banque += mise*1.5
        return result
    elif len(main_j)<len(main_c) and score(main_j)==21:
        result=True
        banque += mise*1.5
        return result
    elif len(main_c)==2 and score(main_c)==21:
        banque -= mise*1.5
        result=False
        return result
    elif len(main_c)<len(main_j) and score(main_c)==21:
        banque -= mise*1.5
        result=False
        return result
    elif score(main_j)>21:
        result=False
        banque -= mise
        return result
    elif score(main_c)>21:
        banque += mise
        result=True
        return result
    else:
        return

def score(carte): #fonction de comptage du score que donne les cartes en main
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

def distrib_cartes(deck,nb_cartes): #distribuer le nombre de carte demandé
    main = []
    for i in range(nb_cartes):
        carte = deck.pop(0)
        main.append(carte)
    return main

def hit(): #fonction donnant la possibilité au joueur de hit
    global deck
    global main_j
    carte=distrib_cartes(deck,1)
    main_j.append(carte[0])



def jouer_croupier(): #fonction faisant jouer le croupier selon la règle de la banque tire a 16 et reste a 17
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

def stand(): #fonction permettant au joueur de stand
    global main_c
    while score(main_c) < 17:
        carte = deck.pop(0)
        main_c.append(carte)
    if score(main_c) > 21:
        return True
    elif score(main_c) == 21:
        return False
    elif score(main_c) > score(main_j):
        return False
    elif score(main_c) < score(main_j):
        return True
    else:
        return False 
        
def abandon(): #fonction permettant au joueur d'abandonner
    global main_j
    for i in range(3):
        main_j.append(10)  
        
def mise(): #fonction permettant au joueur de miser 
    mise_min=1000
    if mise<mise_min:
        return
        val=v_min+1000
def mise_multi_10(): #multiplication de la mise par 10
    val=val*10
    return
def mise_multi_2(): #multiplication de la mise par 2
    val=val*2
    return
def mise_multi_5(): #multiplication de la mise par 5
    val=val*5

def nouveu_deck(): # Creation d'une nouvelle partie et d'un nouveau deck de cartes
    global deck
    deck=nouveau_deck()
    return 
    
def nouvelle_partie(): #fonction de nouvelle partie 
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
mise = 100  
banque = 1000

while win(main_j,main_c,mise) != True: # fonction permettant de jouer dans la console 
    print('Main joueur:',main_j)
    print('Main croupier:',main_c)
    print('Score joueur:',score(main_j))
    print('Score croupier:',score(main_c))
    print('Voulez-vous tirer une carte ? (oui/non)')
    choix = input()
    if choix == 'oui':
        hit()
        if win(main_j,main_c,mise) == True:
            print('Vous avez gagné !')
            break
        elif win(main_j,main_c,mise) == False:
            print('Vous avez perdu !')
            break
    elif choix == 'non':
        #stand()
        if win(main_j,main_c,mise) == True:
            print('Vous avez gagné !')
            break
        elif win(main_j,main_c,mise) == False:
            print('Vous avez perdu !')
            break
print('Votre banque est maintenant de:',banque)


def afficher_carte(frame, carte, position_x): #fonction d'affichage des cartes sur le tapis de jeu #https://fr.python-3.com/?p=1922
    
    chemin_image = f"cards/{carte}.png"
    if chemin_image:
        img = Image.open(chemin_image).resize((60,100))  
        photo = ImageTk.PhotoImage(img)

        
        label = tk.Label(frame, image=photo)
        label.image = photo  
        label.pack(side=tk.LEFT,padx=position_x,pady=10)

def fermer(): #fonction de fermeture de la première fenêtre
        racine.destroy()
        return
def jouer(): # fonction de début de partie
    fermer()
    jeu()


def jeu(): # deuxième interface de jeu 
    racine2=tk.Tk()
    racine2.title("interface de jeu")
    racine2.geometry("1800x1300")
    racine2.configure(bg='darkgreen')
    frame_c= tk.Frame(racine2, bg='darkgreen')
    frame_c.pack(pady=20)
    frame_j= tk.Frame(racine2,bg='darkgreen')
    frame_j.pack(pady=20)
    position= tk.Label(frame_c,text='main croupier')
    position.pack()
    deck=cartes_deck()
    main_j = distrib_cartes(deck,2)
    main_c = distrib_cartes(deck,2)
    afficher_carte(frame_j, main_j[0],10)
    afficher_carte(frame_j, main_j[1],11)
    afficher_carte(frame_c,main_c[0],10)
    afficher_carte(frame_c, main_c[1],11)
    racine2.mainloop()


racine = tk.Tk()  #création de l'interface de la page d'accueil
racine.title("Blackjack - Page d'accueil")
racine.geometry("800x600")
racine.configure(bg="darkgreen")  

titre = tk.Label(racine, text="🃏 BLACKJACK 🃏", font=("Helvetica", 40, "bold"), fg="white", bg="darkgreen")
titre.pack(pady=50)

emojis = tk.Label(racine,text="♠  ♣  ♥  ♦  Atteignez 21 sans dépasser !  ♠  ♥  ♣  ♦",font=("Helvetica", 18),fg="white",bg="darkgreen")
emojis.pack(pady=20)

accroche = tk.Label(racine,text="🎰 Faites vos jeux... Et espérez remporter la mise ! 🎰",font=("Helvetica", 20),fg="white",bg="darkgreen")
accroche.pack(pady=15)

bouton_jouer = tk.Button(racine,text="▶ JOUER",font=("Helvetica", 25, "bold"),bg="white",fg="black",padx=20,pady=10,command=jouer)
bouton_jouer.pack(pady=60)

footer = tk.Label(racine,text="Cliquez sur 'JOUER' pour démarrer la partie",font=("Helvetica", 12),fg="white",bg="darkgreen")
footer.pack(side="bottom", pady=20)
racine.mainloop()

    








