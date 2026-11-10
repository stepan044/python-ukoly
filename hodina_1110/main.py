print("==SIMULACE PRO CISARE FRIDRICHA II. ==")
mesice=int(input("na kolik mesicu ma byt simulace? :"))
a = 1
b = 1 
pocet_mesicu=0
dokonceno=False

while dokonceno == False:
    pocet_mesicu+=1

    if pocet_mesicu==mesice:
        dokonceno = True 

    if pocet_mesicu > 2:
           temp = a + b 
           a = b
           b = temp

    print("")
    print(f"mesic{pocet_mesicu}: {b}par(u) | "+"🐇"*b)
            
print("")
print(f"na ciserskem ostrove bude celkem {b} paru")