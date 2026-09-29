# ************************
# Kalkulačka spropitného
# 29.9.2026
# ************************

print("Vítejte v kalkulačce spropitneho")
celkova_castka = float(input("Zadej celkovou částku účtu: "))
spropitne = int(input("zadej spropitné v %: "))
pocet_lidi = int(input("zadej počet lidí u stolu: "))

spropitne_Kc = celkova_castka * spropitne / 100
celkova_castka += spropitne_Kc
zaplacena_castka = round(celkova_castka / pocet_lidi, 2)

print(f"zaplatíš 1/{pocet_lidi} z {celkova_castka} Kč  ({zaplacena_castka}Kč) ")

