# #Fonction qui en fonction du genre salut différement
# def say_hello(genre):
#     if genre == "M" :
#         print("Hello Boy")
#     elif genre == "F" :
#         print("Hello Girl")
#     else :
#         print("Error 404")
#
# genre = input("M or F : ")
# say_hello(genre)
#Fonction qui trouve le plus petit des 2 nombres
# def minimum(a, b):
#     if a <= b :
#         return a
#     return b
# n1 = int(input())
# n2 = int(input())
# print(minimum(n1, n2))

def dessiner_carre(cote):
    for first_cote in range(cote + 1):
        print("X ", end="")
    print()
    for ligne in range (0, cote, 6):
        print("X ", end = "")

dessiner_carre(3)