from function import *

mot = ChoixMot()
print(mot)
Jeu(mot)
while input("Rejouer (oui/non)").upper() == "OUI":
    mot = ChoixMot()
    Jeu(mot)



