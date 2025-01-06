phrase =  str(input("Ecrivez une phrase: "))
n = len(phrase)
nbre_de_voyelle = 0
for i in range(0,n):
    if phrase[i] in [ "a", "e", "i", "o", "u", "y", "A","E","I","O","U","Y"]:
        nbre_de_voyelle = nbre_de_voyelle+1
print(f"Votre phrase contient {nbre_de_voyelle} de voyelles")
