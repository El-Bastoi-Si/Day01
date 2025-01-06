notes_separees = input("Entrez les notes séparées par des virgules : ")
notes = [float(note) for note in notes_separees.split(',')]
moyenne = sum(notes) / len(notes)
print("La moyenne des notes est :", moyenne)
