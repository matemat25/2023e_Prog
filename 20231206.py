import random

lst = []
i = 0
n = 20

# 1. Feladat: Tölts fel egy listát véletlen számokkal (egy szám csak egyszer szerepeljen!)
print("\n======================= 1. Feladat =======================")
for i in range(n):
    r = random.randint(1,100)
    if r not in lst:
        lst.append(r)
print(lst)

# 2. Feladat: Irasd ki visszafelé: szám > 50 és 3-al osztható?
print("======================= 2. Feladat =======================")

for i in range(len(lst)-1, -1, -1):
    if lst[i] > 50 and lst[i] % 3 == 0:
        print(lst[i], end = ", ")

# 3. Feladat: 3-mal osztható számok átlaga
print("\n======================= 3. Feladat =======================")

osszeg = 0
db = 0
for r in lst:
    if r % 3 == 0:
        osszeg += r
        db += 1
atlag = osszeg / db
print("3-mal osztahtó számok átlaga:",atlag)

# 4. Feladat: Írasd ki azokat a páratlan számokat amelyeknek mindkét szomszédja páros!
print("======================= 4. Feladat =======================")

for i in range(1, len(lst) - 1):
    if lst[i] % 2 != 0 and lst[i-1] % 2 == 0 and lst[i+1] % 2 == 0:
        print(lst[i], end =", ")

# 5. Feladat: Írasd ki azokat a szám párokat amelyek összege páros! Hány ilyen pár van?
print("\n======================= 5. Feladat =======================")

count = 0
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if (lst[i] + lst[j]) % 2 == 0:
            print(lst[i], lst[j])
            count += 1
print("A páros összegű számpárok száma:", count)