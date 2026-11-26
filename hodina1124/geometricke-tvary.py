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


def nevyplneny_obdelnik(stranaA, stranaB):
    radek = 0
    while radek < stranaB:
        if radek == 0 or radek == stranaB - 1:
            print(stranaA * "*")
        else:
            print("*" + " " * (stranaA - 2) + "*")
        radek += 1

def nevyplneny_obdelnik2(stranaA, stranaB):
    radek = 0
    while radek < stranaB:
        if radek == 0 or radek == stranaB - 1:
            print(stranaA * "*")
        else:
            print("*" + " " * (stranaA - 2) + "*")
        radek += 1

def levy_trojuhelnik(vyska):
    radek = 1
    while radek <= vyska:
        print(radek * "*")
        radek += 1

def pravy_trojuhelnik(vyska):
    radek = 1
    while radek <= vyska:
        mezery = vyska - radek
        print(" " * mezery + radek * "*")
        radek += 1

def rovnoramenny_trojuhelnik(zakladna):
    if zakladna % 2 != 0:
        hvezdicky = 1
    else:
        hvezdicky = 2
    
    mezery = (zakladna - hvezdicky) // 2
    
    while hvezdicky <= zakladna:
        print(" " * mezery + "*" * hvezdicky)
        mezery -= 1
        hvezdicky += 2

print("Kreslim geometricke tary slozene ze znaku hvezdicka")

pokracovat = True
while pokracovat:
    typ = input("jaky obraz chces vykreslovat? (c, o, on, cn, tp, tpp,tr): ")
    if typ == "c":
        ctverec(5)
    elif typ == "o":
        obdelnik(3, 4)
    elif typ == "on":
        nevyplneny_obdelnik(5, 4 )
    elif typ == "cn":
        nevyplneny_obdelnik2(5, 5)
    elif typ == "tp":
        vyska = int(input("Jak vysoký má být? "))
        levy_trojuhelnik(vyska)
    elif typ == "tpp":
        vyska = int(input("Jak vysoký má být? "))
        pravy_trojuhelnik(vyska)
    elif typ == "tr":
        zakladna = int(input("Zadej délku základny: "))
        rovnoramenny_trojuhelnik(zakladna)
        print("musis urcit jeden ze znamych tvaru. (c, o, on, cn, tp, tpp, tr)")
        
    odpoved = input("chces vykreslit dalsi obrazec? (a/n): ").lower()
    if odpoved != "a": 
        pokracovat = False