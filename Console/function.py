import random
from Pendu import *

def ChoixMot():
    """
    Description : choisi un mot aléatoirement depuis le fichier
    Sortie : mot (str)
    """
    return random.choice(open("dico.txt","r").read().split())

def AfficheListe(liste):
    """
    Description : (Procédure) affiche les composant d'une liste à la suite
    Entrée : liste (list)
    Sortie : None
    """
    for lettre in liste:
        print(lettre, end=" ")
    print("\n")

def Jeu(mot):
    """
    Description : (Procédure) lance le jeu, vérifie l'input et affiche les messages en conséquences
    Entrée: mot (str)
    Sortie : None
    """
    motCache = "_" * len(mot)
    trouve = False
    lettres_essayees = []       # Variables
    nbrEssai = 0
    
    print("Le Jeu du Pendu")
    print(dessinPendu(nbrEssai))    # Début
    print(motCache)
    
    while not trouve and nbrEssai < 6: # Assure les limites du jeu
        essai = input("Rentrez une lettre").upper()
        print("Vos essais :")
        AfficheListe(lettres_essayees)
        
        if essai.isalpha() and len(essai) == 1: # Vérifie la validité de l'essai
            if essai not in mot:
                print(f"La lettre {essai} n'est pas dans le mot")
                nbrEssai += 1                           
                lettres_essayees.append(essai)
            elif essai in lettres_essayees:                             # Agis en fonction de si l'essai est ou non dans le mot
                print("Vous avez déjà essayé cette lettre :", essai)
            else:
                print(f"La lettre {essai} est dans le mot")
                lettres_essayees.append(essai)
                motCacheEnListe = list(motCache)
                
                for i in range(len(mot)):
                    if mot[i] == essai:
                        indice = i                          # Modifie le mot caché pour rajouter la lettre trouvée
                        motCacheEnListe[indice] = essai
                
                
                motCache = "".join(motCacheEnListe)
                
                if "_" not in motCache:
                    trouve = True
        else:
            print("L'essai n'est pas valide")
        
        print(dessinPendu(nbrEssai))
        print(motCache)
        
    if trouve:
        print("Tu as gagné !")
    else:
        print(f"Perdu ! Le mot était {mot}")
                
                
        