print("Enter the number to be reversed")
a = input()
if int(a) >0:
    a = a[::-1]
else:
    a = a[0] + a[:0:-1]
print("The reversed number : " + str(a))
