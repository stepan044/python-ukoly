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

print("Kreslim geometricke tary slozene ze znaku hvezdicka")

pokracovat = True
while pokracovat:
    typ = input("jaky obraz chces vykreslovat? (c, o, on, cn): ")
    if typ == "c":
        ctverec(5)
    elif typ == "o":
        obdelnik(3, 4)
    elif typ == "on":
        nevyplneny_obdelnik(5, 4 )
    elif typ == "cn":
        nevyplneny_obdelnik2(5, 5)
        print("musis urcit jeden ze znamych tvaru. (c, o, on, cn)")
        
    odpoved = input("chces vykreslit dalsi obrazec? (a/n): ").lower()
    if odpoved != "a": 
        pokracovat = False