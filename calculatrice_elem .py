a = float(input("entrer un nombre : "))
b = float(input("entrer un  second nombre : "))
choix = input("Entrer ton choix  (+, - , * , /) :")
if choix == "+":
    resultat = a + b
    print(f" le resultat est{resultat}  ")
elif choix == "-":
    resultat = a - b
    print(f" le resultat est{resultat}  ")
elif choix == "*":
    resultat = a * b
    print(f" le resultat est{resultat}  ")
elif choix == "/":
    if b ==0:
        print("Error by divisoon is impossible ")
    else:
            resultat = a / b
            print(f"le resultat est {resultat}")
else:
    print("choix impossible")
