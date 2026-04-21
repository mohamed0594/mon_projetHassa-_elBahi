import math
a = float(input("veuillez entrer un nombre a :"))
b =float(input("veuillez entrer un nombre b :"))
c = float(input("veuillez entrer un nombre c :"))

delta = b**2-4*a*c
if delta < 0:
    print("il n'y a pas de solutions ")
elif delta ==0:
    x = (-b)/(2*a)
    print("le resultat est ", x)
else:
    x1 = (-b-math.sqrt(delta))/(2*a)
    x2 = (-b+math.sqrt(delta))/(2*a)
    print("le resultat est ", x1, x2)


