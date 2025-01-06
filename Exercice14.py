nombre = int(input("Entrez un nombre entier naturel : "))

if nombre < 0:
    print("La factorielle n'est définie que pour les entiers naturels.")
elif nombre == 0:
    factorielle = 1
    print("La factorielle de 0 est :", factorielle)
else:
    factorielle = 1
    for i in range(1, nombre+1):
        factorielle *= i
    print("La factorielle de", nombre, "est :", factorielle)
