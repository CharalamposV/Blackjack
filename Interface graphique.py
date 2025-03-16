import tkinter as tk 

racine=tk.Tk()
racine.title("Page d'acceuil, BlackJack")
CANVAS_HEIGHT,CANVAS_WIDTH=1200,800
racine.configure(bg="green")

tapis=tk.Canvas(racine,bg="green",height=CANVAS_HEIGHT,width=CANVAS_WIDTH)
tapis.pack()

salutation= tapis.create_text(CANVAS_WIDTH//2,50,text="Bienvenue au BlackJack !")

bouton_jouer=tk.Button(racine,text="JOUER",font=("helvetica","30"))
bouton_jouer=tapis.create_window(CANVAS_HEIGHT//2,CANVAS_WIDTH//2,window=bouton_jouer)


#bouton_frame = tk.Frame(racine, bg="green")
#bouton_hit = tk.Button(bouton_frame, text= "Hit!", font=("Helvetica", 16), command=hit)
#bouton_stand = tk.Button(bouton_frame, text= "Stand!", font=("Helvetica", 16), command=stand)

