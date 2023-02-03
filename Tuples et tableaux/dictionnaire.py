un_dico = {}
un_dico = {'com' : 'commercial', 'edu' : 'education', 'org' :
'organisation', 'gov' : 'gouvernement américain'}
print(un_dico)
dico_2 = {x : x**2 for x in (2, 4, 6)}
dico_3 = {cle : cle * 2 for cle in ("a", "b", "c")}
dico_4 = dict([('ecran',299),('ordinateur',799),('souris',49)])
print(dico_2)
print(dico_3)
print(dico_4)
prenom=['johan','nathan','didier']
infos=[['78-02-20',175],['90-10-02',180],['66-12-30',161]]
dico_5 = dict(zip(prenom,infos))
nb_elements = len(un_dico)
print(nb_elements)
print(dico_5)
un_dico['fr'] = 'France'
un_dico['edu'] = 'éducation'
del(un_dico['gov'])
une_chaine = un_dico['org']
print(une_chaine)
print(un_dico)
x = un_dico.get('gov', 'rien')
if 'fr' in un_dico:
 print("la clé existe dans le dictionnaire.")
else:
 print("la clé est introuvable dans le dictionnaire.")
for extension in un_dico:
    print(extension)
 # on peut aussi utiliser un_dico.keys()
for nom_de_domaine in un_dico.values():
    print(nom_de_domaine)
for extension, nom_de_domaine in un_dico.items():
    print(extension, nom_de_domaine)
    