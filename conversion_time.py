temps =  int(input("Entrer un temps  en secondes:"))
heure = temps // 3600
minutes = (temps % 3600)//60
secondes = temps % 60
print(f"Il est {heure} heures {minutes} minutes et {secondes} secondes")


