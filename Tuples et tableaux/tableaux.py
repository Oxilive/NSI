# une liste : collection mutable de différents objets
ma_liste = [1,2.3,"a",True]
# une liste vide
ma_liste_vide = []
# une liste de 5 zéros
ma_liste_nulle = 5 * [0]
print(ma_liste)
print(ma_liste[0]) # le premier élément
print(ma_liste[-1]) # le dernier élément
print(ma_liste[1:3]) # une portion de ma liste
print(len(ma_liste)) # la longueur de ma liste
print(ma_liste[len(ma_liste)-1]) # le dernier élément V2
print(type(ma_liste)) # affiche le type de l'objet
# On peut ajouter ou supprimer un élément
ma_liste.append(6)
# pour supprimer à partir de sa valeur
ma_liste.remove(2.3)
# pour supprimer à partir d'un indice
del ma_liste[2]
# On peut ajouter une liste au bout d'une liste
ma_liste.extend(["z",4.5,False,-19,"toto"]) # la liste initiale a été modifiée
# ou bien concaténer deux listes
ma_liste_2 = ma_liste + ["z",4.5,False,-19,"toto"]
print(ma_liste) # la liste initiale n'a pas été modifiée
print(ma_liste_2)
ma_liste = [1,2.3,"a",True]
# On peut parcourir une liste pour agir sur chacun de ses éléments
for element in ma_liste:
    print(element," de type ",type(element))
for i in range(10):
    print(i)
for i in range(1,11):
    print(i)
for i in range(0, 21 , 2):
    print(i)