import random

n = 20
lst = []
for i in range(n):
    r = random.randint(1,50)
    lst.append(r)
print(lst)

print("---min keresés---")
print("1. megoldás")
minn = lst[0]
i_m = 0
for i in range(1, n):
    if lst[i] < minn:
        minn = lst[i]
        i_m = i

print("min: ", minn)
print("i_m: ", i_m)

print("2. megoldás")
minn = lst[0]
for x in lst:  
if x < minn:
    minn = x
print("min: ", minn)
print("3. megoldás")
minn = lst[0]
i = 1
while i < n:
    if lst[i] < minn:
        minn = lst[i]
    i += 1
print("min: ", minn)