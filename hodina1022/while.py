vek = int(input("zadej vek"))
while vek<18 and vek>=0:
    print("jsi nezletily")
    vek = int(input("opakuj zadani veku ( ukonciim zapornou hodnotou): "))
if (vek>=18):
    print("pristup povolen")
else:
    print("pristup neni povolen")

