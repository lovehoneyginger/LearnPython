print("Enter the intervals")
a , b = int(input()),int(input())
print("The prime nos are ")
for i in range(a,b+1):
    for j in range(2,int(i/2) +1):
        if i % j ==0:
            break
    else:
        print(i)
