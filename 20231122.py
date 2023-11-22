import random

i = 0
n = 10
lst = []
r = 100
while  i  <  n:
    r = random.randint(1, 100)
    if r not in lst:
        lst.append(r)
        i += 1
print(lst)
    
print("------------------------------------ 3-mal osztható elemek ------------------------------------")
db = 0
for i in lst:
    if i % 3 == 0:
        print(i, end = ", ")
        db += 1
print("\ndb: ", db)
print("------------------------------------ utlsó számjegye > 5 ------------------------------------")
for i in lst:
    if i % 10 > 5:
        print(i, end = ", ")
print("\n")

print("------------------------------------ lista megfordítása ------------------------------------")
for i in range(len(lst)//2):
    lst[i], lst[len(lst) - 1 - i] = lst[len(lst) - 1 - i], lst[i]
print(lst)
print("------------------------------------ lista rendezés ------------------------------------")
