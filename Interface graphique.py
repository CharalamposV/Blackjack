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


#bouton_frame = tk.Frame(racine, bg="green")
#bouton_hit = tk.Button(bouton_frame, text= "Hit!", font=("Helvetica", 16), command=hit)
#bouton_stand = tk.Button(bouton_frame, text= "Stand!", font=("Helvetica", 16), command=stand)

