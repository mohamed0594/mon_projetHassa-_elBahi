import math
xA = float(input("Entrer la valeur de Xa :"))
yA = float(input("Entrer la valeur de yA :"))
xB = float(input("Entrer la valeur de XB :"))
yB = float(input("Entrer la valeur de yB :"))
# distanceA_B =math.sqrt((xB-xA)**2 + (yB-yA)**2)
# print(f" La distance entre a et b est:{distanceA_B} metre")
distance_A_B = math.hypot(xB-xB,yB-yA)
print(f"la distance de a et b est : {distance_A_B}")