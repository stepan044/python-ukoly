import math

#kontrola prvocisla
je_prvocislo = True

print("kontrola prvocisla")
cislo = int(input("zadej cele cislo: "))

if cislo < 2:
    je_prvocislo = False
elif cislo == 2:
    je_prvocislo = True
elif cislo % 2 == 0:
    je_prvocislo = False
else:
    delitel=3
    while delitel <= int(math.sqrt(cislo)):
        if cislo % delitel == 0:
            je_prvocislo = False
            break
        delitel += 2

if je_prvocislo:
    print(f"Číslo {cislo} je prvnocsiclem.")
else:
    print(f"Číslo {cislo} neni prvocislem.")