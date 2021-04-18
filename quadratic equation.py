import cmath
print("Enter the a, b, c in the equation ax^2 + bx + c = 0")
a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))
print("solution x1 : " + str(((-b) + cmath.sqrt(b**2 - 4*a*c))/(2*a)))
print("solution x2 : " + str(((-b) - cmath.sqrt((b**2) - (4*a*c)))/(2*a)))
