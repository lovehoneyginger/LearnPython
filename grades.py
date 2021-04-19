print("Enter the marks of 5 subjects")
a,b,c,d,e = float(input()),float(input()),float(input()),float(input()),float(input())
f = (a+b+c+d+e)/5
if f>=90:
    print("The grade : A+")
elif f>=80:
    print("The grade : A")
elif f>=70:
    print("The grade : B+")
elif f>=60:
    print("The grade : B")
elif f>=50:
    print("The grade : C+")
elif f>=40:
    print("The grade : C")
else:
    print("Failed")
