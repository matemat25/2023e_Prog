
print("----------1. Fleadat----------")
import random
i= 0
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

