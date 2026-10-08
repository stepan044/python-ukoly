x_panacka = int(input("zadej souradnici X"))
y_panacka = int(input("zadej souradnici Y"))

#nebezpecna plocha (kolizni oblast)
x1 = 2
x2 = 6
y1 = 2
y2 = 5

# test, zda doslo ke kolizi
if x_panacka>=x1 and x_panacka<=x2 and y_panacka>=y1 and y_panacka<=y2:
    print("kolize") 
else:
    print("objekt mimo kolizni zonu....")