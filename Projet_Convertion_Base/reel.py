from naturel import*
# Fonction qui permet convertir une mantisse sur 32 ou 64 bit-
def convertir_mantisse_bin(nombre, nombre_bit):
    # Affectation à la variable cote decimale une chaine de caractere vide
    cote_decimal = ""
    # Condition si le nombre de bit est à 32 sépare la partie décimale et entière
    if nombre_bit == 32:
        cote_entier = convertir_entier_bin(int(nombre))
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
        cote_entier = convertir_entier_bin(int(nombre))
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
    cote_entier = convertir_entier_bin(int(nombre))
    nb_mantisse = convertir_mantisse_bin(nombre, nombre_bit)
    #calcul de l'exposant en fonction de la valeur du décalage et du nombre de bit
    if nombre_bit == 32:
        exposant = len(cote_entier) + 127 - 1
        exposant = convertir_entier_bin(exposant)
    if nombre_bit == 64:
        exposant = len(cote_entier) + 1023 - 1
        exposant = convertir_entier_bin(exposant)
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

