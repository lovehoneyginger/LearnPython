print("Enter any number")
a = int(input())
b = str(a)
sum = 0
c = []
while a>0:
    c = a%(10)
    sum = sum+(c**len(b))
    a //=10
if sum == int(b):
    print("Amstrong number")
else:
    print("Not an Amstrong number")
