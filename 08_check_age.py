a = int(input("quel est ton anné de naissance? "))
a = 2026 - a
print(f"tu as {a}")
if a < 12:
    print("tu es un enfant")
elif a >= 12 and a <17:
    print("tu es un adolescent")
else :
    print("tu es un adulte")
    