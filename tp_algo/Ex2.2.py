nombre_choisi = int(input())
if nombre_choisi < 0 :
    nombre_choisi = -nombre_choisi
quotient = nombre_choisi//2
pair = quotient * 2
for i in range(quotient + 1):
    print(pair)
    pair -= 2
