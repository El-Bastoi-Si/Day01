import random 
nbre = random.randint(1,100)
nbre_utilisateur = int(input("Devinez un nombre entre 1 à 100: "))
if nbre_utilisateur <nbre:
    print("Votre nombre est petit")
elif nbre_utilisateur>nbre:
    print("Votre nombre est grand")
else: 
    print("Bravo vous avez gagné !")

