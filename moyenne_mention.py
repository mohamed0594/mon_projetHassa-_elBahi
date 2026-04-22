note1= float(input("Entrer la premiere note : "))
note2= float(input("Entrer la  deuxieme  note : "))
note3= float(input("Entrer la  troisieme note : "))
if (0 <= note1 <= 20) and (0 <= note2 <= 20)  and (0 <= note3 <= 20): 
   moyenne_annuelle = (note1 + note2 +note3)/3
   if moyenne_annuelle >= 16:
    print(f"vous avez obtenu la mention Tres bien {moyenne_annuelle}")
   elif 14 <= moyenne_annuelle <=16 :
     print(f"vous avez obtenu la mention Bien{moyenne_annuelle}")
   elif 12 <= moyenne_annuelle <=14:
      print(f"vous avez obtenu la mention Assez Bien {moyenne_annuelle}",)
   elif 10 <= moyenne_annuelle <= 12:
     print(f"vous avez obtenu la mention Passable {moyenne_annuelle}",)
   elif moyenne_annuelle < 10:
     print(f"vous avez obtenue une note insuffissante {moyenne_annuelle}")
   else:
     print("vous devriez saisir  des notes comprises entre(0, 20)")

     
