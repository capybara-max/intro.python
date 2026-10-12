print("""Bienvenue dans ce programme pour calculer les moyennes
tape "q" pour avoir le resultat final.
""")
a = input("Insère une note sur 20 : ")
b = 0
c = 20
M = 0
while a != "q":
    if int(a) < 0 or int(a) > 20 :
        print("valeur top basse ou trop haute")
        a = input("Insère une note sur 20 : ")
    elif not a.isnumeric():
        print("valeur invalide")
        a = input("Insère une note sur 20 : ")
    else:
        b = b + int(a)
        M = b / c+20
        a = input("Insère une note sur 20 : ")
        
        
    
if M > 10 :
    print(f"Voici ta moyenne {M} tu as REUSSI !")
elif M == 10:
    print(f"Voici ta moyenne {M} tu doit faire attention !")
else :
    print(f"Voici ta moyenne {M} tu aurait pu faire mieux !")
    