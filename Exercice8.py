
nbr1=float(input("Donner le premier nombre: "))
nbr2=float(input("Donner le deuxieme nombre: "))
nbr3=float(input("Donner le troisieme nombre: "))
if nbr1>=nbr2 and nbr1>=nbr3:
     print(f"La plus nomnre le plus grand  est {nbr1}")
elif  nbr2>=nbr1 and nbr2>=nbr3:
        print(f"La plus nomnre le plus grand  est {nbr2}")
elif nbr3>=nbr2 and nbr3>=nbr1:
        print(f"La plus nomnre le plus grand  est {nbr3}")
else :
        print("les nombres que vous avez saisi sont egaux :")
