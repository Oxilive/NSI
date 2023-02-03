# Exercice 3 sur les dictionnaires
# version a completer

# lecture du fichier texte sous forme d'une chaine de caractères
fichier = open('nom_du_fichier.txt', 'r')
texte = fichier.read()
fichier.close()
   
# mise en minuscules
texte = texte.lower()

# retrait de la ponctuation et caractères spéciaux
for caract in ['.', ',', ';', ':', '!', '?', '-', "'", '"', '(', ')', '§', '\t', '\n', '$', '£',
               '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
    texte = texte.replace(caract, ' ')

# retrait des accents
for accent in ['é', 'è', 'ê', 'ë']:
    texte = texte.replace(accent, 'e')

for accent in ['à', 'â', 'ä']:
    texte = texte.replace(accent, 'a')

for accent in ['ö', 'ô']:
    texte = texte.replace(accent, 'o')

for accent in ['ï', 'î']:
    texte = texte.replace(accent, 'i')

for accent in ['ù', 'û', 'ü']:
    texte = texte.replace(accent, 'u')

# et des cédilles
texte = texte.replace('ç', 'c')

# création du dictionnaire
dico = {}

# décompte des lettres
"""
partie à completer :
vous devez rempir le dictionnaire avec des cles correspondant aux lettres du texte
et des valeurs indiquant le nombre de fois ou chaque lettre apparait.
"""


"""
fin de la partie a completer.
"""

# retrait de la clé espace
del dico[' ']

print(dico)

# on peut transformer en liste python pour trier
liste = [(lettre, freq) for lettre, freq in dico.items()]
liste.sort()

print(liste)
