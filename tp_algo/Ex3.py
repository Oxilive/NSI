nb_choisi = int(input())**2
while nb_choisi <= 1000000 :
    print(nb_choisi)
    nb_choisi -= 1
    while nb_choisi >= -1000000 :
        nb_choisi -= 1
        print(nb_choisi)
