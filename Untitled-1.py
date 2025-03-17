#Trouvé sur internet, ->pour s'en inspirer, Interface graphique fonctions et variables pas complètes
#finir de def les variables (tk, creer_paquet)
class BlackjackApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Jeu de Blackjack")

        self.paquet = creer_paquet()
        self.main_joueur = [self.paquet.pop(), self.paquet.pop()] #fois 2
        self.main_croupier = [self.paquet.pop(), self.paquet.pop()]

        self.canvas = tk.Canvas(root, width=600, height=400, background="green")
        self.canvas.pack()

        self.afficher_cartes()

        self.bouton_tirer = tk.Button(root, text="Tirer une carte", command=self.tirer_carte)
        self.bouton_tirer.pack(side=tk.LEFT, padx=20)

        self.bouton_rester = tk.Button(root, text="Rester", command=self.rester)
        self.bouton_rester.pack(side=tk.LEFT, padx=20)

        self.message = tk.Label(root, text="Tour du joueur", bg="green", fg="white")
        self.message.pack()

  








