a = 2
b = 3 
c = 1 

if a >b:
    temp = a
    a = b 
    b = temp

if b > c: 
    temp = b 
    b = c 
    c = temp

if b > c:
    temp = b
    b = c
    c = temp

print (f"a = {a}, b = {b}, c = {c}")