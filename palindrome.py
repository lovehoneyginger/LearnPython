print("Enter the number to check")
a = input()
for i in range(0,int(len(a)/2)):
    if a[i] != a[len(a)-i-1]:
        print("Not a palindrome")
        break
else:
    print("Its a palindrome")
