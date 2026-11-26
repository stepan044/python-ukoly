def cifra_na_znak(hodnota):
    cifry = "0123456789ABCDEF"
    return cifry[hodnota]  # opraveno: hranaté závorky místo kulatých


def preved_soustavu(cislo, zaklad):
    podporovane_zaklady = [2, 8, 10, 16]

    if cislo < 0 or zaklad not in podporovane_zaklady:
        return None

    if cislo == 0:
        return "0"

    vysledek = ""
    temp = cislo
    while temp > 0:
        zbytek = temp % zaklad
        vysledek = cifra_na_znak(zbytek) + vysledek
        temp = temp // zaklad

    return vysledek  


print("Převodní tabulka IT číselných soustav:")
print(f"{'DEC':<6} | {'BIN':<8} | {'OCT':<6} | {'HEX':<6}")
print("-" * 34)

aktualni_cislo = 0
while aktualni_cislo <= 16:
    dec_val = str(aktualni_cislo)
    bin_val = preved_soustavu(aktualni_cislo, 2)
    oct_val = preved_soustavu(aktualni_cislo, 8)
    hex_val = preved_soustavu(aktualni_cislo, 16)

    print(f"{dec_val:<6} | {bin_val:<8} | {oct_val:<6} | {hex_val:<6}")
    aktualni_cislo += 1

print("-" * 34)

test_zaporne = preved_soustavu(-5, 2)
test_zaklad = preved_soustavu(15, 3)

print(f"Test neplatného cisla:", preved_soustavu(-3, 2))
print(f"Test neplatného základu:", preved_soustavu(10, 5))