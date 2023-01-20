#Boucle qui ajoutera 1 à x tant qu'il est < que 10
x = 0
while (x < 10):
   x += 1
   print(x)
#Boucle infini tant que x n'est pas supérieur ou égale à 10
x = 0
while True:
    x += 1
    print(x)
    if (x >= 10):
        break
#Boucle borné avec la fin non compris [0 , 10[
for i in range(0, 10):
    print(i)
#Boucle borné avec la fin non compris avancant de 2 en 2[5 , 15 , 2[
for j in range(5, 15, 2):
    print(x)