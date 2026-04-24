annee = int(input(" Entrer une annee "))
if(annee%4 ==0 ) and (annee%100!=100 or (annee%400==0)) :
    print("c'est une annee bissextile")
else: 
     print(" ce n'est pas une annee bissextile")


