import random
# tajne_cislo = random.randint(1,20)
tajne_cislo = 19
pocitadlo = 0 
tip = 0
max_pokusu = 5

print(f"hadej cele cislo o 1 do 20 mas na to {max_pokusu} pokusu")

while tip!=tajne_cislo and pocitadlo<max_pokusu:
    tip = int(input("zadej svuj: "))
    if tip>=1 and tip<=20:
         pocitadlo += 1
         if tip>tajne_cislo:
             print("moje cislo je mensi")
         elif tip<tajne_cislo:
             print("moje cislo je vetsi")
    

if tip==tajne_cislo:
    print(f"uhadl jsi cislo {tajne_cislo} na {pocitadlo} pokusu")
else:
    print(f"prekrocil jsi {max_pokusu} pokusu. cislo bylo {tajne_cislo}.")