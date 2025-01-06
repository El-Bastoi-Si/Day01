nbre1 = float(input("Donnez le premier nombre: "))
nbre2 = float(input("Donnez le deuxième nombre: "))
addition = nbre1+nbre2
multiplication = nbre1*nbre2
division = nbre1/nbre2
utilisateur = input("Quelle genre de calcul souhaitez vous faire: +,-,*,/")
if utilisateur ==  "+":
    print(f"L'addition de {nbre1} et {nbre2} est de {addition} ")
elif utilisateur == "*":
        print(f"la multiplication  de {nbre1} et {nbre2} est de {multiplication} ")
elif utilisateur == "/":
          print(f"La division de {nbre1} et {nbre2} est de {division} ")

else:
       print("Calcul inconnu")
