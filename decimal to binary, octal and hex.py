print("Enter the number to be converted")
a = float(input())
a1 = int(a)
a2 = a - a1

a11 =a1
c =""
while(a11>0):
    b = a11%2
    c = c +str(b)
    a11//=2


a22 = a2
e = ''
i = 0
while(a22!=0 and i!=10):
    i +=1
    a22 = a22*2
    e = e + str(int(a22))
    if a22>1:
        a22 = a22-1
print("Binary equivalent")
print(c[::-1],".",e[::])

a33 =a1
f =""
while(a33>0):
    b = a33%8
    f = f +str(b)
    a33//=8

a44 = a2
g = ''
i = 0
while(a44!=0 and i!=10):
    i +=1
    a44 = a44*8
    g = g + str(int(a44))
    a44 = a44 - int(a44)
print("Octal equivalent")
print(f[::-1],".",g[::])

a55 =a1
h =""
while(a55>0):
    b = a55%16
    if b>9:
        if b == 10:
            h = h + "A"
        elif b == 11:
            h = h + "B"
        elif b == 12:
            h = h + "C"
        elif b == 13:
            h = h + "D"
        elif b == 14:
            h = h + "E"
        elif b == 15:
            h = h + "F"
    else:
        h = h +str(b)
    a55//=16

a66 = a2
j = ''
i = 0
while(a66!=0 and i!=10):
    i +=1
    a66 = a66*16
    b = int(a66)
    if b>9:
        if b == 10:
            j = j + "A"
        elif b == 11:
            j = j + "B"
        elif b == 12:
            j = j + "C"
        elif b == 13:
            j = j + "D"
        elif b == 14:
            j = j + "E"
        elif b == 15:
            j = j + "F"
    else:
        j = j +str(b)
    a66 = a66 - int(a66)
print("Octal equivalent")
print(h[::-1],".",j[::])
