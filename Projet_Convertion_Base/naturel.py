def convertir_entier_bin(entier):
    # Initialisation de mon résultat sous forme de chaîne de caractere et du bool
    binaire = ""
    bool = -1
    # Bouble non-bornée
    while bool !=0:
        # Technique des divisions successives par 2 dont on récupère le reste qu'on ajoute au résultat
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
