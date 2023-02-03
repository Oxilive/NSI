from random import *
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
L1 = boucle_nb_random()
L1.append(77)
L1.append(74)
L1.remove(77)
L3 = [100,25,15,40]
L4 = [20,9,4,7]
L5 = [40,29,14,7,15]
if __name__ == '__main__':
    mon_image = bitmap_image(10,10)
    # print(choisir_main(32, game))
    # print(game)
    # print(mon_image)
    # print_image(mon_image)
    # print(boucle_nb_random())
    # print(boucle_nb_random2())
    # print(L1)
    # print(L3[2])
    # print(L3[3])
    # print(len(L4))
    # print(L4[-1])
    # print(L5[1:4])
    # print(L5[-3])
    # print(moyenne_liste(L4))
    Li = (boucle_nb_random_li_de_li(5,3))
    print(acceder_nieme(Li,1,3))
    