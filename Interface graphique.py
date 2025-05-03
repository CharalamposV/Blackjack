import tkinter as tk 
CANVAS_HEIGHT,CANVAS_WIDTH=800,800

def fermer():
        racine.destroy()
        return
def jouer():
    fermer()
    racine2=tk.Tk()
    racine2.title("interface de jeu")
    #racine.iconbitmap("icone jeu.jpg")
    racine2.geometry("1000x600")
    tapis = tk.Canvas(racine2,height="500",width="800",bg="green")
    tapis.pack()

racine=tk.Tk()
racine.title("Page d'acceuil, BlackJack")
tapis=tk.Canvas(racine,bg="green",height=CANVAS_HEIGHT,width=CANVAS_WIDTH)
tapis.pack()
salutation= tapis.create_text(CANVAS_WIDTH//2,50,text="Bienvenue au BlackJack !")

bouton_jouer=tk.Button(racine,text="JOUER",font=("helvetica","15"),command=jouer)
bouton_jouer=tapis.create_window(CANVAS_HEIGHT//2,CANVAS_WIDTH//2,window=bouton_jouer)
racine.mainloop()


racine2=tk.Tk()
racine2.title("interface de jeu")
racine2.geometry("1000x600")
tapis = tk.Canvas(racine2,height="500",width="800",bg="green")
tapis.pack()
bouton_hit=tk.Button(racine2,text="   HIT   ",command=hit, font=32)
bouton_hit.pack()

racine2.mainloop()



######################################### PAGE D'ACCUEIL #############################################
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
######################### page de fin 
def re_jouer():
    print("Voulez vous rejouez ?")
    racine.destroy()
def quitter():
    racine.destroy()
#bouton_frame = tk.Frame(racine, bg="green")
#bouton_hit = tk.Button(bouton_frame, text= "Hit!", font=("Helvetica", 16), command=hit)
#bouton_stand = tk.Button(bouton_frame, text= "Stand!", font=("Helvetica", 16), command=stand)

