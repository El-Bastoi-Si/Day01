import random
import string

def generer_mot_de_passe(longueur):
    minuscules = string.ascii_lowercase
    majuscules = string.ascii_uppercase
    chiffres = string.digits
    symboles = string.punctuation
    somme_caracteres = minuscules + majuscules + chiffres + symboles
    mot_de_passe = ''.join(random.choice(somme_caracteres) for _ in range(longueur))
    return mot_de_passe
longueur = int(input("Entrez la longueur de votre mot de passe : "))
mot_de_passe = generer_mot_de_passe(longueur)
print("Votre mot de passe aléatoire est :", mot_de_passe)
