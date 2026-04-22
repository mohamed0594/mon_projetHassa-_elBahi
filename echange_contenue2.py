a = int(input("Entrer un nombre svp  NB1:"))
b = int(input("Entrer un nombre svp NB2:"))

if a*b > 0:
  a,b = b,a
else:
  a = a +b
  b = a * b  

print(f"La nouvelle valeur de a est {a}")
print(f"La nouvelle valeur de b est {b}")



