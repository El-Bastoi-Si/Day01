def trier():
  """Trie les notes entrées par l'utilisateur."""

  liste_de_nombre = input("Entrez les notes séparées par des virgules : ")
  nombre = [int(float(note)) for note in liste_de_nombre.split(',')]  # Convert strings to numbers
  nombre.sort()
  print("Liste de notes triée :", nombre)

trier()
