resist1 = float(input("entrer la premiere resistance :"))
resist2= float(input("entrer la  deuxieme resistance :"))
resist3 = float(input("entrer la troisieme resistance :"))
resist4 = float(input("entrer la  quatrieme resistance :"))
resistance_serie = resist1 +resist2 +resist3
resistance_derivation = (resist1*resist2*resist3)/resist1*resist2 +resist1*resist3+resist2*resist3
print(f" la resistance en serie est :{resistance_serie}")
print(f"la resistance en derivation est :{resistance_derivation}") 