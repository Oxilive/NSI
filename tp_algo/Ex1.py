print("Renseigner votre prénom ci dessous")
prenom = input()
print("Donner votre genre avec F ou H")
sexe = input()
if sexe == "H" :
    print("Bonjour Monsieur", prenom)
elif sexe == "F" :
    print("Bonjour Madame", prenom)
else:
    print("Bonjour", prenom)
    