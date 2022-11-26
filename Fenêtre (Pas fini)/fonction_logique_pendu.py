import random
from main import *
from Pendu import *

def ChoixDuMot():
    """
    Description : choisi un mot aléatoirement depuis le fichier
    Sortie : mot (str)
    """
    return random.choice(open("dico.txt","r").read().split())

lettresrentrees = []

texteMotCache = ["_" * len(mot)] 
essai = 0
gameOverMessage = "Perdu, le mot était " + mot

def ValideLettre() : 
    """ 
    """
    global essai
    global texteMotCache
    global graphique
    global entree
    global LARGEUR_DE_CANVAS
    global HAUTEUR_DE_CANVAS
    global boiteInput
    global COULEUR_DE_FOND
    
    lettre = entree.get().upper()
    
    #assert lettre.isalpha() == True
    
    
    lettresrentrees.append(lettre=entree.get())
    
    for i in range(len(mot) + 1):
        if mot[i] == lettre:
            texteMotCache[i] = lettre
        else:
            essai += 1
            graphique.forget()
            graphique.create_text(LARGEUR_DE_CANVAS/2, HAUTEUR_DE_CANVAS/2, text=dessinPendu(essai), fill="white", font=("Helvetica", 30))
            graphique.pack()
            if essai == 6:
                boiteInput.forget()
                perdu = Label(boiteInput, text="Perdu", font=("Helvetica", 20), bg=COULEUR_DE_FOND, fg="white")
                perdu.pack(side=TOP)
                boiteInput.pack()
            
            
            
    
            

