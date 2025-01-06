import random

nombre_mystere = random.randint(1, 1000)
nb_essais = 10

print("J'ai choisi un nombre entre 1 et 1000. Tu as 10 essais pour le trouver.")

for essai in range(1, nb_essais+1):
    proposition = int(input(f"Essai {essai} : "))

    if proposition < nombre_mystere:
        print("C'est plus !")
    elif proposition > nombre_mystere:
        print("C'est moins !")
    else:
        print(f"Félicitations, tu as trouvé le nombre mystère en {essai} essais !")
        break

if proposition != nombre_mystere:
    print(f"Dommage, tu n'as pas trouvé. Le nombre mystère était {nombre_mystere}.")
