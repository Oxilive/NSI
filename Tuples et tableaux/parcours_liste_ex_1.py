from random import*
def create_list_random():
    liste = []
    for loop in range(100):
        choix = randint(1, 10000)
        liste.append(choix)
    return liste
liste = create_list_random()
# print(list)
def what_little_list(liste):
    minimum = float("inf")
    indice = 0
    for nombre in liste:
        if nombre < minimum:
            minimum = nombre
            position = indice 
        indice += 1 
    return(minimum ,position)
minimum = what_little_list(liste)
# print(what_little_list(liste))
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
# print(look_duplicates(liste))
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
game = create_jeu_carte()
# print(choisir_main(32, game))
# print(game)
def bitmap_image(nblignes, nbcolonnes,):
    return [[0]*nbcolonnes] * nblignes
def print_image(tableau):
    hauteur = len(tableau)
    largeur = len(tableau[0])
    for y in range(hauteur):
        for x in range(largeur):
            print(tableau[y][x], end=" ")
        print()
def tracer_trait()
if __name__ == '__main__':
    mon_image = bitmap_image(10,10)
    # print(mon_image)
    print_image(mon_image)