import itertools
print("Enter any three numbers")
a ,b,c = int(input()) ,int(input()),int(input())
l = list(itertools.permutations([a,b,c]))
print(l)
