def est_palindrome(mot):
  mot = mot.lower()  # On met tout en minuscules pour ne pas tenir compte de la casse
  return mot == mot[::-1]  # On compare le mot à son inverse

mot = input("Entrez un mot : ")
if est_palindrome(mot):
  print("C'est un palindrome !")
else:
  print("Ce n'est pas un palindrome.")
