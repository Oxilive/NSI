#Link inter fichier
from reel import *
from naturel import *
from relatifs import *
loop = True
while loop == True:
    # Début de l'interface IHM
    # Affichage des choix possibles pour l'utilisateur
    print("Si vous choisissez 1, vous coderez des naturels")
    print("Si vous choisissez 2, vous coderez des relatifs")
    print("Si  vous choisissez 3, vous coderez des réels")
    Choix = int(input("Quel choix voulez-vous faire:"))
    print()
    if Choix == 1:
        # Affichage des possibilités si choix == 1
        print("Si vous voulez convertir de binaire à entier, tapez 1")
        print("Si vous voulez convertir de entier à binaire, tapez 2")
        print("Si vous voulez convertir de entier à hexadécimal, tapez 3")
        Choix = int(input("Si vous voulez quitter, tapez 4, sinon, tapez 0:"))
        orientation = int(input("Que voulez-vous:"))
        print()
        if orientation == 1:
            parametre = input("entrez votre binaire:")
            print(convertir_bin_entier(parametre))
            Choix = int(input("Si vous voulez quitter, tapez 4, sinon, tapez 0:"))
        if orientation == 2:
            parametre = int(input("Entrez votre entier:"))
            print(convertir_entier_bin(parametre))
            Choix = int(input("Si vous voulez quitter, tapez 4, sinon, tapez 0:"))
        if orientation == 3:
            parametre = int(input("Entrez votre entier:"))
            print(convertir_entier_hexa(parametre))
            Choix = int(input("Si vous voulez quitter, tapez 4, sinon, tapez 0:"))
    if Choix == 2:
        # Affichage des possibilités si choix == 2
        print("Si vous voulez convertir un entier signé en binaire, tapez 1")
        print("Si vous voulez convertir du binaire à un entier relatif, tapez 2")
        Choix = int(input("Si vous voulez quitter, tapez 4, sinon, tapez 0:"))
        orientation1 = int(input("Que voulez-vous:"))
        if orientation1 == 1:
            parametre = int(input("Entrez votre relatif:"))
            print(conv_relatif_bin(parametre))
            Choix = int(input("Si vous voulez quitter, tapez 4, sinon, tapez 0:"))
        if orientation1 == 2:
            parametre = input("Entrez votre binaire:")
            print(conv_bin_relatif(parametre))
            Choix = int(input("Si vous voulez quitter, tapez 4, sinon, tapez 0:"))
    if Choix == 3:
        # Affichage des possibilités si choix == 3
        print("Si vous voulez coder des flottants en binaire sur 32 ou 64 bits, tapez 1")
        print("Si vous voulez décoder un binaire sur 32 ou 64 bits en flottants, tapez 2")
        Choix = int(input("Si vous voulez quitter, tapez 4, sinon, tapez 0:"))
        orientation2 = int(input("Que voulez-vous:"))
        if orientation2 == 1:
            parametre = float(input("Entrez votre flottant:"))
            nombre_bit = int(input("Sur quel nombre de bits voulez coder (32 ou 64):"))
            print(coder_flottant(parametre, nombre_bit))
            Choix = int(input("Si vous voulez quitter, tapez 4, sinon, tapez 0:"))
        if orientation2 == 2:
            parametre = input("Entrez votre binaire:")
            nombre_bit = int(input("Entrez le nombre de bit sur lequel le binaire est codé:"))
            print(decoder_flottant(parametre, nombre_bit))
            Choix = int(input("Si vous voulez quitter, tapez 4, sinon, tapez 0:"))
    if Choix == 4:
        # Possibilité de sortie qui permet de sortir de la boucle
        loop = False










