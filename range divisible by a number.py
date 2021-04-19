print("Enter the range [a,b]")
a , b = int(input()) ,int(input())
print("Enter the divisor")
c = int(input())
print("The numbers are : ")
for i in range(a,b+1):
    if i % c==0:
        print(str(i))
