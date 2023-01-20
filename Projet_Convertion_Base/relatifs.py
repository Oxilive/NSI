
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

