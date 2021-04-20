print("Enter the digit for which the multiplication table is to be displayed")
a = int(input())
for i in range(0,11):
    print(str(a) + "*" + str(i) + "=" + str(a*i))
