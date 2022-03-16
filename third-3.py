import random

print("input n")
n=int(input())
a=[]

for i in range(n):
    a.append(random.randint(0, 3200))
print(a)    