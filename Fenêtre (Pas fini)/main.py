from tkinter import *
from Pendu import dessinPendu
from fonction_logique_pendu import *

mot = ChoixDuMot()
COULEUR_DE_FOND = "#23272A"
HAUTEUR_DE_CANVAS = 350         # Variables
LARGEUR_DE_CANVAS = 450


root = Tk()     # Création de la fenêtre

root.title("Pendu")
root.geometry("1920x1080")              # Configuration de la fenêtre
root.minsize(480, 360)
root.config(background=COULEUR_DE_FOND)

boiteGraphique = Frame(root, bg=COULEUR_DE_FOND)    # Création de la boîte qui contiendra le dessin et le mot

graphique = Canvas(boiteGraphique, bg=COULEUR_DE_FOND, height=HAUTEUR_DE_CANVAS, width=LARGEUR_DE_CANVAS, bd=0, highlightthickness=0)
graphique.create_text(LARGEUR_DE_CANVAS/2, HAUTEUR_DE_CANVAS/2, text=dessinPendu(0), fill="white", font=("Helvetica", 30))
graphique.pack()

motCache = Label(boiteGraphique, text=texteMotCache, font=("Helvetica", 20), bg=COULEUR_DE_FOND, fg="white")
motCache.pack()

boiteGraphique.pack(side=TOP) 

boiteInput = Frame(root, bg=COULEUR_DE_FOND) # Création de la boîte qui contiendra l'input et la liste des lettres déjà rentrées

entree = Entry(boiteInput, font=("Helvetica", 20), bg="white", fg=COULEUR_DE_FOND) # Création de la zone où l'on entre les lettres
entree.pack(side=TOP)

bouton = Button(boiteInput, text="Valider la lettre", font=("Helvetica", 20), bg=COULEUR_DE_FOND, fg="white", command=ValideLettre)
bouton.pack(side=TOP)

boiteInput.pack()

root.mainloop()
