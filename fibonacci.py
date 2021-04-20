print("Enter the length of fibonacci series")
a = int(input())
b = 0
c = 1
print("The fibonacci series")
for i in range(0,a):
    print(str(b))
    d = b
    b = c
    c = c + d
