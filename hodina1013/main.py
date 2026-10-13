#vstupy
pocet = float(input("Počet osob: "))
student = input("Je student? (ano/ne): ")
vek = float(input("Věk osob: "))

#vyhodnoceni typu vstupenky
cena_zaklad = 500
nazev_slevy = ""

if pocet >= 4: #pravdlo, ktere ma vyssi prioritu nez vek
    cena_celkem = pocet * cena_zaklad * 0.75
    nezev_slevy = "skupinova sleva"
else:                 #vekova pravidla (student nebo senior)
     if vek<26 and student == "ano":
        cena_celkem = pocet * cena_zaklad * 0.7
        nazev_slevy = "studentska sleva"
     elif vek>=65 : 
         cena_celkem = pocet *cena_zaklad * 0.8
         nazev_slevy = "sleva pro seniory"
     else:
         cena_celkem = pocet * cena_zaklad 


#vystupy
print("cena celkova: ", cena_celkem)
print("cena jedne vstupenky: ",cena_celkem/pocet)
if nazev_slevy!="" :
  print(nazev_slevy) 