print("Enter the year to check")
a = int(input())
if a%4==0:
    if a%100==0:
        if a%400==0:
            print("Leap Year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")
