age = int(input("entrer votre age svp : "))
if  6 <= age <=7 :
    print("il s'agit d'une categorie de Poussin")
elif 8 <= age <= 9:
    print("il s'agit d'une categorie de Pupille")
elif 10 <= age <= 11:
    print("Il s'agit d'une categorie Minime")
elif age > 12:
    print("Il s'agit d'un cadet")
else:
    print(" vous n'etes pas dans cette categories")
