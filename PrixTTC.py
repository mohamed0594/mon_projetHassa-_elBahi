# prix_hors_taxe = float(input("Entrer le prix hors taxe : "))
# categorie = input("Entrer sa categorie A,B,C : ")
# if categorie == "A " :
#     TVA = 7/100
# elif categorie == "B" :
#     TVA = 20/100
# elif categorie == "C":
#     TVA = 25/100

# prix_TTC = prix_hors_taxe*(1  + TVA) 
# print(f" Le prix TTc est {prix_TTC} FCFA")

    
#   Methode avec les dictionnaires  #

prixHT= float(input(" Entrer le prix Hors taxe :"))
cat = input("Entrer la categorie :")
tva_dict = {
    "A":7/100,
    "B":20/100,
    "c":25/100
}  
prixTTC = prixHT*(1+ tva_dict[cat])
print(f"le prix TTc est {prixTTC}")