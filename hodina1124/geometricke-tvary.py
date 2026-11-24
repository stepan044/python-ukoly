def ctverec(strana):
    radek = 0 
    while radek < strana:
        print(strana * "*")
        radek += 1 

def obdelnik(stranaA, stranaB):
    radek = 0
    while radek < stranaB:
       print(stranaA * "*")
       radek += 1

# Nevyplněný obdélník s pevně zadanými stranami (např. a=5, b=3)
def nevyplneny_obdelnik(stranaA, stranaB):
    radek = 0
    while radek < stranaB:
        if radek == 0 or radek == stranaB - 1:
            print(stranaA * "*")
        else:
            print("*" + " " * (stranaA - 2) + "*")
        radek += 1


print("Kreslim geometricke tary slozene ze znaku hvezdicka")

pokracovat = True
while pokracovat:
    typ = input("jaky obraz chces vykreslovat? (c, o, on): ")
    if typ == "c":
        ctverec(5)
    elif typ == "o":
        obdelnik(3, 4)
    elif typ == "on":
        nevyplneny_obdelnik(5, 4 )# Tady si rovnou zadej rozměry, jaké chceš (např. šířka 6, výška 3)
    else: 
        print("musis urcit jeden ze znamych tvaru. (c, o, on)")
        
    odpoved = input("chces vykreslit dalsi obrazec? (a/n): ").lower()
    if odpoved != "a": 
        pokracovat = False