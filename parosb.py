import random

print("lista feltöltése véletlen számokkal")
n = 20
lst = []
for i in range(n):
    r = random.randint(1,50)
    lst.append(r)
print(lst)
print("---páros számok keresése listában---")
print("1. megoldás")

for x in lst:
    if x % 2 == 0:
        print(x, end = ", ")
     
print("2. megoldás")
for i in range(n):
    if lst[i] % 2 == 0:
        print(lst[i] , end = ", ")
     
print("3. megoldás")
i = 0
while i < n:
    if lst[i] % 2 == 0:
        print(lst[i] , end = ", ")
    i += 1
print("---legnagyobb páros szám keresése a listában---")
maxx = 2
for x in lst:
    if x % 2 == 0:
        if x > maxx:
            maxx = x
print("max páros", maxx)
