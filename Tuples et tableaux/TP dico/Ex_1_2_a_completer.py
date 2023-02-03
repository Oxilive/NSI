# dico_eleve = {'Léo':['Génie', 'Maths','Physique'], 'Mael': ['Idiot', 'Maths','Physique']}
# dico_eleve["Armand"] = ['Maths', 'SES', 'Physique']
# dico_eleve['Armand'][2] = 'HGGSP'
# print(dico_eleve)



# Points au Scrabble

# dico_scrabble = {"A" : 1, "B" : 3, "C" : 3, "D" : 2, "E" : 1, "F" : 4, "G" : 2,
#                  "H" : 4, "I" : 1, "J" : 8, "K" : 10, "L" : 1, "M" : 2, "N" : 1,
#                  "O" : 1, "P" : 3, "Q" : 8, "R" : 1, "S" : 1, "T" : 1, "U" : 1,
#                  "V" : 4, "W" : 10, "X" : 10, "Y" : 10, "Z" : 10}
# mot = str(input())
# def points(mot):
#     point = 0
#     for lettre in mot:
#         point = point + dico_scrabble[lettre]
#     return point
# print(points(mot))
# reponse_alice = {"Q1":"b","Q2":"a","Q3":"d","Q5":"b"}
# def corriger_qcm(reponse_eleve):
#     note = 0
#     AWNSER = {"Q1":"c","Q2":"a","Q3":"d","Q4":"c","Q5":"b"}    
#     for reponse in reponse_eleve:
#         if reponse_eleve[reponse]== AWNSER[reponse]:
#             note += 3
#         if reponse_eleve[reponse]!= AWNSER[reponse]:
#             note -= 1
#         if note < 0:
#             note = 0
#     return note
# print(corriger_qcm(reponse_alice))

# dico_conv = {"GBP": 0.84828,
#              "USD": 1.1193,
#              "JPY": 121.75,
#              "CHF": 1.0865,
#              "RUB": 69.1898}
# def conv_monnaie(valeur,monnaie_depart,monnaie_arriver):
#     return round(valeur * dico_conv[monnaie_depart] / dico_conv[monnaie_arriver], 2)
# print(conv_monnaie(15,"USD","CHF"))
def compter_lettre(texte):
    lettre = {'a' : 0 , 'b' : 0 , 'c' : 0 , 'd' : 0}