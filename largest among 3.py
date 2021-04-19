print("Enter any 3 numbers")
a,b,c = int(input()),int(input()),int(input())
if a>b and a>c:
    print("The largest : " + str(a))
elif b>a and b>c:
    print("The largest : " + str(b))
else:
    print("The largest : " + str(c))
