#vstupy
pocet = int(input("Zadejte počet osob: "))

if pocet < 4:
    student = input("Jste student? (ano/ne): ").lower()
    vek = int(input("Zadejte věk: "))

den = input("Zadejte den v týdnu: ").lower()


#vyhodnoceni typu vstupenky
if den in ("sobota", "neděle", "nedele"):
    cena_zaklad = 550
    typ_predstaveni = "Víkendové představení"
else:
    cena_zaklad = 500
    typ_predstaveni = "Běžné představení"

nazev_slevy = ""
sleva_procent = 0

if pocet >= 4:  #pravidlo, ktere ma vyssi prioritu nez vek
    koeficient = 0.75
    nazev_slevy = "Skupinová sleva"
    sleva_procent = 25
else:           #vekova pravidla (student nebo senior)
    if vek < 26 and student == "ano":
        koeficient = 0.7
        nazev_slevy = "Studentská sleva"
        sleva_procent = 30
    elif vek >= 65:
        koeficient = 0.8
        nazev_slevy = "Sleva pro seniory"
        sleva_procent = 20
    else:
        koeficient = 1

cena_jedne = cena_zaklad * koeficient
cena_celkem = cena_jedne * pocet


#vystupy
print("\n--- Výsledná účtenka ---")
print(f"Typ lístku: {pocet} osoba ({typ_predstaveni})" if pocet == 1
      else f"Typ lístku: {pocet} osob ({typ_predstaveni})")
if nazev_slevy != "":
    print(f"Druh slevy: {nazev_slevy} ({sleva_procent} %)")
else:
    print("Druh slevy: žádná")
print(f"Cena za 1 vstupenku: {cena_jedne:.2f} Kč")
print(f"Celková cena: {cena_celkem:.2f} Kč")