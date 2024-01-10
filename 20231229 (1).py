
print("----------1. Fleadat----------")
import random
i = 0
lst = []
for i in range(20):
    szam = random.randint(1,50)
    lst.append(szam)
print(lst)

print("----------2. Fleadat----------")
# Kérj be egy számot a klaviatúráról!
szám = int(input("Kérem adjon meg egy számot: "))

legjobb1 = lst[0]
legjobb2 = lst[1]


for i in range(len(lst)):
    if abs(lst[i] - szám) < abs(legjobb1 - szám):
        legjobb2 = legjobb1
        legjobb1 = lst[i]
    elif abs(lst[i] - szám) < abs(legjobb2 - szám):
        legjobb2 = lst[i]

# Írd ki a legjobb értékeket
print("A legjobban megközelítő értékek:", legjobb1, "és", legjobb2)

print("----------3. Fleadat/ 1. megoldás----------")

for i in range(len(lst)):
    db = 0  # Számláló a jelenlegi érték előfordulásainak számolására
    for j in range(len(lst)):
        if lst[i] == lst[j]:
            db += 1  # Ha egyezik az érték, növeljük a számlálót
    if db > 1:
        print(lst[i], ":", db, "alkalommal szerepel")

#2. megoldás
print("----------3. Fleadat/ 2. megoldás----------")
i = 0
while i < len(lst):
    j = i + 1
    db = 1  # Minden egyes elem előfordulása, beleértve az aktuálisat is
    while j < len(lst):
        if lst[i] == lst[j]:
            db += 1
        j += 1
    if db > 1:
        print(lst[i], ":", db, "alkalommal szerepel")
    i += 1

print("---------- 4. Fleadat ----------")

legkisebb = lst[0]

for elem in lst:
    if elem < legkisebb:
        legkisebb = elem

print(legkisebb)

legkisebbek = []

for i in range(3):
    legkisebb = lst[0]
    for elem in lst:
        if elem < legkisebb and elem not in legkisebbek:
            legkisebb = elem
    legkisebbek.append(legkisebb)

print(legkisebbek)

n = 2
legkisebbek = []

for i in range(n):
    legkisebb = lst[0]
    for elem in lst:
        if elem < legkisebb and elem not in legkisebbek:
            legkisebb = elem
    legkisebbek.append(legkisebb)

print(legkisebbek)


print("---------- 5. Fleadat ----------")

n = len(lst)
for i in range(n):
    for j in range(0, n-i-1):
        if lst[j] % 2 == 0 and lst[j+1] % 2 == 0:
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
        elif lst[j] % 2 != 0 and lst[j+1] % 2 != 0:
            if lst[j] < lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

print(lst)







