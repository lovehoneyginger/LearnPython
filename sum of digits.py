print("Enter a number")
a = int(input())
sum=0
while a>0:
    b = a%10
    sum += b
    a = a//10
print("The sum of digits : " + str(sum))
