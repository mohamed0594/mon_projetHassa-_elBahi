copies  = int(input(" Entrer  Le nombre de copies :  "))
if copies <= 10:
    prix = copies*0.30
elif copies <=30:
    prix = (10 * 0.30) +(copies-10)*0.25
else:
    if copies > 30:
        prix = (10 *0.30) +(20*0.25) + (copies-30)*0.20

print( f" La facture correspondante est {prix} FCFA")

