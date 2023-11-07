
import random

print("lista feltöltése véletlen számokkal")
n = 20
lst = []
for i in range(n):
    r = random.randint(1,50)
    lst.append(r)
print(lst)
print("---max keresés---")
print("1. megoldás")
maxx = lst[0]
for x in lst:
    if x > maxx:
        maxx = x
print("max: ", maxx)  

print("2. megoldás")
maxx = lst[0]
for i in range(1, n):
    if lst[i] > maxx:
        maxx = lst[i]
print("max: ", maxx)

print("3. megoldás")
maxx = lst[0]
i = 1
while i < n:
    if lst[i] > maxx:
        maxx = lst[i]
    i += 1
print("max: ", maxx)
