print("Enter the range ")
a,b = int(input()),int(input())
for i in range(a,b+1):
    if i%2!=0:
        print(str(i) + " ",sep = " ",end=" ")
