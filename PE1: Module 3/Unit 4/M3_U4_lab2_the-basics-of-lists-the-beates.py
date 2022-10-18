beatles = []

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

for i in range(2):
    newMember = input("Give me the name of one of the remaining members: ")
    beatles.append(newMember)
del beatles[-2]
del beatles[-1]
beatles.insert(0, "Ringo Starr")


# probando la longitud de la lista
print("Los Fav", len(beatles))