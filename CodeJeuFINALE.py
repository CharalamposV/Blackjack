from random import shuffle
from tkinter import messagebox
import tkinter as tk
from PIL import Image,ImageTk

def cartes_deck():
    couleur = ['carreau','coeur','pique','trefle']
    valeur = ['as','2','3','4','5','6','7','8','9','10','valet','dame','roi']
    deck=[{"valeur": v,"couleur": c} for c in couleur for v in valeur]
    shuffle(deck)
    return deck

def win(main_j,main_c,mise):
    global banque
    result=False
    if len(main_j)==2 and score(main_j)==21:
        banque += mise*1.5
        messagebox.showinfo("Blackjack!!","Tu as gagné avec un Blackjack naturel")
        page_fin()
        return True
    elif len(main_j)<len(main_c) and score(main_j)==21:
        banque += mise*1.5
        messagebox.showinfo("Blackjack!!","Tu as gagné")
        page_fin()
        return True
    elif len(main_c)==2 and score(main_c)==21:
        banque -= mise
        messagebox.showinfo("Défaite","Le croupier a un Blackjack naturel")
        page_fin()
        return False
    elif len(main_c)<len(main_j) and score(main_c)==21:
        banque -= mise
        messagebox.showinfo("Défaite","Le croupier a un Blackjack")
        page_fin()
        return False
    elif score(main_j)>21:
        banque -= mise
        messagebox.showinfo("Défaite","Tu as bust")
        page_fin()
        return False
    elif score(main_c)>21:
        banque += mise*1.5
        messagebox.showinfo("Victoire","Le croupier a bust")
        page_fin()
        return True
    elif score(main_j)>score(main_c) and score(main_c)>=17:
        banque += mise*1.5
        messagebox.showinfo("Victoire!")
        page_fin()
        return True
    else:
        banque = banque
        messagebox.showinfo("Egalité","Rejoue pour gagner!")
        page_fin()

def score(main): #compter le score que donne les cartes en main
    total = 0
    for carte in main:
        v=carte['valeur']
        if v in ['10','valet','dame','roi']:
            total += 10
        elif v == 'as':
            if total+11 <= 21:
                total +=11
            else:
                total +=1
        else:
            total += int(v)    
    return total

def distrib_cartes(deck,nb_cartes): #distribuer le nombre de carte demandé
    main = []
    for i in range(nb_cartes):
        carte = deck.pop(0)
        main.append(carte)
    return main

def hit():
    global deck
    global main_j
    carte=distrib_cartes(deck,1)
    main_j.append(carte[0])
    afficher_carte(frame_j,main_j[len(main_j)-1],10)

    if score(main_j)>21:
        win(main_j,main_c,mise)



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
        
def mise():
    mise_min=100
    if mise<mise_min:
        val=mise+mise_min
    return
def mise_multi_10():
    global mise
    mise*=10
    return
def mise_multi_2():
    global mise
    mise*=2
    return
def mise_multi_5():
    global mise
    mise*=5
    return

# Creation d'une nouvelle partie
'''def nouveau_deck():
    global deck
    deck=nouveau_deck()
    return '''
    
'''def nouvelle_partie():
    global main_j
    global main_c
    nouveau_deck()
    main_j.clear()
    main_c.clear()
    main_j = distrib_cartes(deck,2)
    main_c = distrib_cartes(deck,2)'''

def stand():
    global main_c, frame_c, bouton_hit, main_j
    bouton_hit.configure(state="disabled")
    while score(main_c) < 17:
        carte = deck.pop(0)
        main_c.append(carte)
        afficher_carte(frame_c,carte,10)
    win(main_j,main_c,mise)
    

deck = cartes_deck()
main_j = distrib_cartes(deck,2)
main_c = distrib_cartes(deck,2)
mise = 100  
banque = 1000
'''while win(main_j,main_c,mise) != True:
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
print('Votre banque est maintenant de:',banque)'''
def page_fin():
    racine_3= tk.Tk()
    racine_3.title("Blackjack - Page de fin")
    racine_3.geometry("600x400")
    racine_3.configure(bg="#8E9189")  
    racine_3.attributes('-topmost', True)
    bouton_re_jouer = tk.Button(racine_3,text="🔄 Rejouer",font=("Helvetica", 25),bg="white",fg="black",padx=20,pady=10,command=lambda: [racine_3.destroy(),racine2.destroy(),main()])
    bouton_re_jouer.pack(pady=20)
    bouton_quitter=tk.Button(racine_3,text="❌ Quitter",font=("Helvetica", 25),bg="white",fg="black",padx=20,pady=10,command=lambda : [racine_3.destroy(),racine2.destroy()])
    bouton_quitter.pack(pady=50)
    bouton_hit.configure(state="disabled")
    bouton_stand.configure(state="disabled")
    bouton_ff.configure(state="disabled")


    if banque > 0:
        messagebox.showinfo("Résultat", f"Tu as actuellement : {banque} euros")
    '''elif banque < 0:
        messagebox.showinfo("Résultat", f"Vous avez perdu la somme de : {abs(banque)} euros")
    else:
        messagebox.showinfo("Résultat", "Vous n'avez rien gagné... Rejouez à nouveau !")'''

    racine_3.mainloop()
def on_select(event):
    global mise
    choix = menu_var.get()

    if choix == "Mise x2":
        mise_multi_2()
    elif choix == "Mise x5":
        mise_multi_5()
    elif choix == "Mise x10":
        mise_multi_10()
    elif choix == "Mise x1":
        mise = 100
    label_var.set(f"Mise actuelle : {mise} €")
    

def afficher_carte(frame, carte, position_x):
    nom_carte = f"{carte['valeur']} de {carte['couleur']}"
    chemin = f"cards/{nom_carte}.png"
    if chemin:
        image = Image.open(chemin).resize((60,100))
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(frame, image=photo)
        label.image = photo
        label.pack(side=tk.LEFT, padx=position_x, pady=10)
def fermer():
        racine.destroy()
        return
def jouer():
    fermer()
    main()
def main():
    global frame_j,frame_c,bouton_hit,bouton_stand,deck,main_j,main_c,bouton_ff,racine2,label_var,menu_var
    racine2=tk.Tk()
    racine2.title("interface de jeu")
    racine2.geometry("1440x920")
    racine2.configure(bg='darkgreen')

    frame_global= tk.Frame(racine2,bg='darkgreen')
    frame_global.pack(expand=True, fill=tk.BOTH)
    
    frame_c= tk.Frame(frame_global, bg='darkgreen')
    frame_c.pack(pady=90)
    
    frame_j= tk.Frame(frame_global,bg='darkgreen')
    frame_j.pack(pady=200)
    
    position= tk.Label(frame_c,text='main croupier')
    position.pack()
    
    position1= tk.Label(frame_j,text='main joueur')
    position1.pack()
    
    deck=cartes_deck()
    main_j = distrib_cartes(deck,2)
    main_c = distrib_cartes(deck,2)
    
    afficher_carte(frame_j, main_j[0],10) 
    afficher_carte(frame_j, main_j[1],11)
    afficher_carte(frame_c,main_c[0],10)
    afficher_carte(frame_c, main_c[1],11)
    
    label_var=tk.StringVar()
    label_var.set(f"Mise actuelle : {mise} €")
    
    frame_boutons = tk.Frame(racine2, bg='darkgreen')
    frame_boutons.pack(side=tk.BOTTOM, fill=tk.X, pady=30)
    
    bouton_ff = tk.Button(frame_boutons, text="Abandon :(", font=("Helvetica", 16), command=page_fin,
                          bg='red', fg='white', padx=20, pady=10)
    bouton_ff.pack(side=tk.LEFT, padx=80)
    
    espace = tk.Label(frame_boutons, text="", bg='darkgreen') 
    espace.pack(side=tk.LEFT, expand=True)
    
    bouton_stand = tk.Button(frame_boutons, text="Stand", font=("Helvetica", 16), command=stand,
                             bg='orange', fg='black', padx=20, pady=10)
    bouton_stand.pack(side=tk.RIGHT, padx=30)
    
    bouton_hit = tk.Button(frame_boutons, text="Hit!", font=("Helvetica", 16), command=hit,
                           bg='lightgreen', fg='black', padx=20, pady=10)
    bouton_hit.pack(side=tk.RIGHT, padx=30)
    
    menu_var = tk.StringVar()
    options = ["Mise x1","Mise x2", "Mise x5", "Mise x10"]
    menu_var.set(options[0])
    dropdown = tk.OptionMenu(frame_boutons, menu_var, *options, command=lambda: on_select())
    dropdown.pack(side=tk.LEFT, padx=10)
    label = tk.Label(frame_boutons, textvariable=label_var, font=("Helvetica",16))
    label.pack(side=tk.LEFT, padx=10)
    button = tk.Button(frame_boutons, text="Mise", command=lambda :on_select(None))
    button.pack(side=tk.LEFT, padx=10)
    racine2.mainloop()
    
   

racine = tk.Tk()
racine.title("Blackjack - Page d'accueil")
racine.geometry("800x600")
racine.configure(bg="darkgreen")  

titre = tk.Label(racine, text="🃏 BLACKJACK 🃏", font=("Helvetica", 40, "bold"), fg="white", bg="darkgreen")
titre.pack(pady=50)

emojis = tk.Label(racine,text="♠  ♣  ♥  ♦  Atteignez 21 sans dépasser !  ♠  ♥  ♣  ♦",font=("Helvetica", 18),fg="white",bg="darkgreen")
emojis.pack(pady=20)

accroche = tk.Label(racine,text="🎰 Faites vos jeux... Et tentez de remporter la mise ! 🎰",font=("Helvetica", 20, "italic"),fg="white",bg="darkgreen")
accroche.pack(pady=15)

bouton_jouer = tk.Button(racine,text="▶ JOUER",font=("Helvetica", 25, "bold"),bg="white",fg="black",padx=20,pady=10,command=jouer)
bouton_jouer.pack(pady=60)

footer = tk.Label(racine,text="Cliquez sur 'JOUER' pour démarrer la partie",font=("Helvetica", 14),fg="white",bg="darkgreen")
footer.pack(side="bottom", pady=20)
racine.mainloop()
