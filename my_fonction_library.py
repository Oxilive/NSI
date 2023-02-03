#Importations des libraries
from random import randint , choice
from math import *
#Fonction convertion binaire flottant hexadécimal
def conv_entier_bin(entier):
    binaire = ""
    bool = -1
    while bool !=0:
        bool= entier//2
        reste = entier%2
        binaire = str(reste) + binaire
        entier = bool
    return binaire
def conversion(reste):
    # table de conversion pour les restes des divisions par 16
    if reste >=0 and reste <= 9:
        reste = str(reste)
    elif reste == 10:
        reste = "A"
    elif reste == 11:
        reste = "B"
    elif reste == 12:
        reste = "C"
    elif reste == 13:
        reste = "D"
    elif reste == 14:
        reste = "E"
    elif reste == 15:
        reste = "F"
    return reste
def convertir_entier_hexa(entier):
    #Initialisation de mon résultat en chaîne de caractere
    hexa = ""
    # Boucle non-bornée
    while entier > 0:
        #Technique des divisions successives par 16 auquel on récupère le reste et qu'on convertit si besoin
        reste = entier %16
        hexa = conversion(reste)+hexa
        entier = entier //16
    return hexa
def convertir_bin_entier(binaire):
    resultat = 0
    puissance = 0
    # Boucle bornée par la longueur de la chaîne, qui commence au rang 0
    for bit in range(len(binaire) - 1, -1, -1):
        # Parcours de chaque bit de la chaîne, si le bit est à 1, on ajoute au résultat le 2 à l'exposant puissance qu'on incrémente à chaque tour
        if binaire[bit] == "1":
            resultat = resultat + 2**puissance
        puissance +=1
        # Si le bit est à 0, on ne change rien au résultat
        if binaire[bit] == "0":
            resultat = resultat
        if binaire[bit] !="0" and binaire[bit] !="1":
            return None
    return resultat
def conv_relatif_bin(entier):
    #Condition pour un codage sur 8 bit
    if entier > 127 or entier < -128:
        entier = 0
        print("Error")
    # Technique du complément à deux pour 8 bit
    if entier < 0:
        entier = 256 + entier
    else:
        x = 0
    binaire = ""
    bool = -1
    # boucle non-bornée pour récupérer le reste grâce à la variable bool, et donc transforme rnotre entier en binaire
    while bool != 0:
        bool = entier // 2
        reste = entier % 2
        binaire = str(reste) + binaire
        entier = bool
    return binaire
def conv_bin_relatif(binaire):
    # Affectation de la position des 0 et 1 dans la variable bit
    bit = binaire[0]
    # Vérification du bit de point fort pour savoir si l'on décode un entier négatif ou positif
    if bit == "1":
        resultat = 0
        puissance = 0
        # Boucle bornée par la longueur de la chaîne, qui commence au rang 0
        for bit in range(len(binaire) - 1, -1, -1):
            # Parcours de chaque bit de la chaîne, si le bit est à 1, on ajoute au résultat le 2 à l'exposant puissance qu'on incrémente à chaque tour
            if binaire[bit] == "1":
                resultat = resultat + 2 ** puissance
            puissance += 1
        resultat = resultat - 2 ** 8
    if bit == "0":
        resultat = 0
        puissance = 0
        # Boucle bornée par la longueur de la chaîne, qui commence au rang 0
        for bit in range(len(binaire) - 1, -1, -1):
            # Parcours de chaque bit de la chaîne, si le bit est à 1, on ajoute au résultat le 2 à l'exposant puissance qu'on incrémente à chaque tour
            if binaire[bit] == "1":
                resultat = resultat + 2 ** puissance
            puissance += 1
            # Si le bit est à 0, on ne change rien au résultat
    return resultat
# Fonction qui permet convertir une mantisse sur 32 ou 64 bit-
def convertir_mantisse_bin(nombre, nombre_bit):
    # Affectation à la variable cote decimale une chaine de caractere vide
    cote_decimal = ""
    # Condition si le nombre de bit est à 32 sépare la partie décimale et entière
    if nombre_bit == 32:
        cote_entier = conv_entier_bin(int(nombre))
        nb_decimal = nombre - int(nombre)
        # Boucle non-bornée afin de transformer la partie décimal en binaire
        compteur = 0
        while nb_decimal != 1.0 and compteur < 23:
            # Compteur qui permet de limiter la mantisse à 23 bit
            compteur = compteur + 1
            #technique de la multiplication par 2 afin de récupérer la partie entière
            nb_decimal = nb_decimal * 2
            cote_decimal = cote_decimal + str(int(nb_decimal))
            if nb_decimal > 1:
                nb_decimal = nb_decimal - 1
        nb_mantisse = cote_entier[1:] + cote_decimal
        #Condition qui rajoute des zéro si jamais la mantisse n'est toujours pas sur 23 bit
        if len(nb_mantisse) < 23:
            for loop in range(23 - len(nb_mantisse)):
                nb_mantisse = nb_mantisse + "0"
            nb_mantisse = nb_mantisse[0:23]
    # Condition si le nombre de bit est à 64
    elif nombre_bit == 64:
        cote_entier = conv_entier_bin(int(nombre))
        nb_decimal = nombre - int(nombre)
        # Boucle non-bornée qui permet de calculer la mantisse en récupérant la partie entière des multiplications successives par 2
        while nb_decimal != 1.0:
            nb_decimal = nb_decimal * 2
            cote_decimal = cote_decimal + str(int(nb_decimal))
            if nb_decimal > 1:
                nb_decimal = nb_decimal- 1

        nb_mantisse = cote_entier[1:] + cote_decimal
        # Condition si jamais le nombre de bit pour la mantisse n'est toujours pas égale à 52 bit
        if len(nb_mantisse) < 52:
            for loop in range(52- len(nb_mantisse)):
                nb_mantisse = nb_mantisse + "0"
        nb_mantisse = nb_mantisse[0:52]
    return nb_mantisse
#fonction qui permet de passer d'un nombre flottant à un nombre binaire
def coder_flottant(nombre, nombre_bit):
    #Signe du nombre
    if float(nombre) >= 0:
        resultat = "0"
    else:
        resultat = "1"
        nombre = nombre * - 1
    cote_entier = conv_entier_bin(int(nombre))
    nb_mantisse = convertir_mantisse_bin(nombre, nombre_bit)
    #calcul de l'exposant en fonction de la valeur du décalage et du nombre de bit
    if nombre_bit == 32:
        exposant = len(cote_entier) + 127 - 1
        exposant = conv_entier_bin(exposant)
    if nombre_bit == 64:
        exposant = len(cote_entier) + 1023 - 1
        exposant = conv_entier_bin(exposant)
    if nombre_bit == 32:
        if len(exposant) > 8:
            print("Ce nombre ne peux pas etre codé sur 32 bits !")
        #Boucle bornée qui permet de coder l'exposant sur 8 bit
        for x in range(8 - len(exposant)):
            exposant = "0" + exposant
    #Condition pour vérifier si le nombrre est bien codé sur 64 bit
    elif nombre_bit == 64:
        if len(exposant) > 11:
            print("Ce nombre ne peux pas etre codé sur 64 bits !")
        #Boucle bornée qui permet de coder l'exposant sur 11 bit
        for x in range(11 - len(exposant)):
            exposant = "0" + exposant
    resultat = resultat + exposant + nb_mantisse
    return resultat
# Fonction pour décoder un binaire flottant codé sur 32 ou 64 bit
def decoder_flottant(nombre, nombre_bit):
    compteur = 0
    mantisse = 0
    if nombre_bit == 32:
        # Condition qui vérifie si le binaire rentré par l'utilisateur n'est pas sur 32 bit
        if len(nombre) != 32:
            print("Le nombre que vous avez rentré n'est pas sur 32 bits")
        #Condition pour vérifier le signe du flottant
        if nombre[0:1] == "0":
            signe = 1
        else:
            signe = -1
        #Application du décalage sur l'exposant convertit en entier sur 32 bit
        exposant = int(nombre[1:9])
        exposant = convertir_bin_entier(str(exposant)) - 127
        #Boucle bornée qui calcule la mantisse du nombre binaire, auquel on incrémente 1
        for bit in nombre[9:]:
            compteur = compteur + 1
            if bit == "1":
                mantisse = mantisse + 2**(-1*compteur)
        mantisse = mantisse + 1
    if nombre_bit == 64:
        # Condition qui vérifie si le binaire rentré par l'utilisateur n'est pas sur 64 bit
        if len(nombre) != 64:
            print("Le nombre que vous avez rentré n'est pas sur 64 bits")
        #Condition qui permet de connaitre le signe du nombre en fonction du premier bit
        if nombre[0:1] == "0":
            signe = 1
        else:
            signe = -1
        exposant = int(nombre[1:12])
        exposant = convertir_bin_entier(exposant) - 1023
        #Boucle bornée qui convertit la mantisse en entier
        for bit in nombre[12:]:
            compteur = compteur + 1
            if bit == "1":
                mantisse = mantisse + 2**(-1*compteur)
        mantisse = mantisse + 1
    resultat = signe * (2**exposant) * mantisse
    return resultat
#Fonction avec calcul de nombres
def what_bigger(a,b):
    if a >= b :
        return a
    return b      
def mettre_mot_verlan(mot):
    mot_a_l_envers = ""
    for lettre in mot:
        mot_a_l_envers =  lettre + mot_a_l_envers 
    return mot_a_l_envers
def est_palinedrome(mot):
    return mettre_mot_verlan(mot) == mot
def pythagore(a,b,c):
    assert a >= 0 and b >= 0 and c >= 0, "Côté Negatif Ou Nul Imposible" 
    assert a + b >= c and c + b >= a and a + c >= b, "Triangle Non Trassable"
    return (a**2 + b**2 == c**2) or (c**2 + b**2 == a**2) or (a**2 + c**2 == b**2)
def est_ce_annee_bissextile(annee):
    assert 1 <= annee <= 2121, "Non Conforme à la plage de valeur comprise entre 1 et 2121"
    if annee % 4 == 0:
        if annee % 100 != 0:
            return True
        elif annee % 100 == 0:
            if annee % 400 == 0:
                return True
    return False
def est_ce_nbpremier(nombre):
    assert type(nombre) == int and nombre > 0, "Vous devez tester pour un entier naturel non nul!"
    if nombre == 1 or (nombre % 2 == 0 and nombre != 2):
        return False
    for diviseur in range(3, int(sqrt(nombre)) + 1 , 2):    
        if nombre % diviseur == 0:
            print("Voici le plus petit diviseur", diviseur)
            return False
    return True
#Fonction avec des tuples
def tuple_division(a,b):
    assert a > b and b > 0
    return (a//b, a%b)
#Fonction avec des listes
def create_list_random():
    liste = []
    for loop in range(100):
        choix = randint(1, 50)
        liste.append(choix)
    return liste
def what_little_list(liste):
    minimum = 10000
    indice = 0
    for nombre in liste:
        if nombre < minimum:
            minimum = nombre
            position = indice 
        indice += 1 
    return(minimum ,position)
def look_duplicates(liste):
    minimum = float("inf")
    indice = 0
    for nombre in liste:
        if nombre < minimum:
            minimum = nombre
            position = [indice] 
        elif nombre == minimum:
            position.append(indice)
        indice += 1
    return(minimum ,position)
def del_duplicates(liste):
    to_delete = []
    for indice, element in enumerate(liste):
        if element in liste[indice + 1:]:
            to_delete.append(element)
    for position in to_delete:
        liste.remove(element)
    return to_delete
def create_jeu_carte():
    liste_cartes = ["7", "8", "9", "10", "valet", "dame", "roi", "as"]
    liste_famille = ["pique", "coeur", "carreau", "trefle"]
    jeu = [carte + "" + famille for carte in liste_cartes for famille in liste_famille]
    return jeu
def choisir_main(n,jeu):
    main = []
    jeu_utile = jeu.copy()
    for i in range(n):
        carte = choice(jeu_utile)
        main.append(carte)
        jeu_utile.remove(carte)
    return main
def bitmap_image(nblignes, nbcolonnes,):
    return [[0]*nbcolonnes] * nblignes
def print_image(tableau):
    hauteur = len(tableau)
    largeur = len(tableau[0])
    for y in range(hauteur):
        for x in range(largeur):
            print(tableau[y][x], end=" ")
        print()
def boucle_nb_random():
    liste = []
    for loop in range(6):
        nombre_random = randint(1,100)
        liste.append(nombre_random)
    return liste
def boucle_nb_random2():
    liste =[randint(1,100)for i in range(7)]
    return liste
def boucle_nb_random_li_de_li(nbliste, nb_in_liste):
    li = []
    for i in range(nbliste):
        liste_random = [randint(1,100)for j in range(nb_in_liste)]
        li.append(liste_random)
    return li
def acceder_nieme(L,n,p):
    return L[p-1][n-1]
def moyenne_liste(liste):
    taille_li = len(liste)
    moyenne = 0
    indice = 0
    while indice != taille_li:
        moyenne = moyenne + liste[indice]
        indice += 1
    moyenne = moyenne // taille_li
    return moyenne
#Fonction avec des dictionnaires
dico_scrabble = {"A" : 1, "B" : 3, "C" : 3, "D" : 2, "E" : 1, "F" : 4, "G" : 2,
                 "H" : 4, "I" : 1, "J" : 8, "K" : 10, "L" : 1, "M" : 2, "N" : 1,
                 "O" : 1, "P" : 3, "Q" : 8, "R" : 1, "S" : 1, "T" : 1, "U" : 1,
                 "V" : 4, "W" : 10, "X" : 10, "Y" : 10, "Z" : 10}
mot = str(input())
def points(mot):
    point = 0
    for lettre in mot:
        point = point + dico_scrabble[lettre]
    return point
reponse_alice = {"Q1":"b","Q2":"a","Q3":"d","Q5":"b"}
def corriger_qcm(reponse_eleve):
    note = 0
    AWNSER = {"Q1":"c","Q2":"a","Q3":"d","Q4":"c","Q5":"b"}    
    for reponse in reponse_eleve:
        if reponse_eleve[reponse]== AWNSER[reponse]:
            note += 3
        if reponse_eleve[reponse]!= AWNSER[reponse]:
            note -= 1
    return note if note < 0 else 0
dico_conv = {"GBP": 0.84828,
             "USD": 1.1193,
             "JPY": 121.75,
             "CHF": 1.0865,
             "RUB": 69.1898}
def conv_monnaie(valeur,monnaie_depart,monnaie_arriver):
    return round(valeur * dico_conv[monnaie_depart] / dico_conv[monnaie_arriver], 2)
#Main Program
# nombre = int(input("Enter positive number: "))
# liste = create_list_random()
# print(conv_entier_bin(nombre))
# print(mettre_mot_verlan("kayak"))
# print(est_palinedrome("kayak"))
# print(pythagore(3,1,5))
# print(est_ce_annee_bissextile(2124))
# print(est_ce_nbpremier(155))
# print(tuple_division(19,3)[0])
# print(what_little_list(liste))
# print(look_duplicates(liste))
# print(del_duplicates(liste))
# game = create_jeu_carte()
# print(game)
# print(boucle_nb_random())
# print(boucle_nb_random2())
# print(points(mot))
# print(corriger_qcm(reponse_alice))
# print(conv_monnaie(15,"USD","CHF"))
