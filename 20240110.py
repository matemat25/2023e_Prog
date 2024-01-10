print("----------1. Fleadat----------")
import random
i = 0
n = 20
lst = []
for i in range(20):
    szam = random.randint(1,50)
    lst.append(szam)
print(lst)

print("----------2. Fleadat----------")


# Szám bekérése a felhasználótól
szám = int(input("Kérem, adjon meg egy számot: "))
minn = 1000
for i in range(n-1):
    for j in range(i+1, n):
        if abs (szám -(lst[i] + lst[j])) <  minn:
            minn = abs (szám - (lst[i] + lst[j]))
            x1 =lst[i]
            x2 = lst[j]
össz = x1 + x2
print(("%.1f + %.i = %.i")%(x1, x2, össz))
print("eltérés: %.i" %(szám - össz))
print(x1 , "+", x2 ,"=", össz)

print("----------3. Fleadat----------")
for i in range(n-1):
    db = 1  # Számláló a jelenlegi érték előfordulásainak számolására
    for j in range(i+1, n):
        if lst[i] == lst[j]:
            db += 1  # Ha egyezik az érték, növeljük a számlálót
    if db > 1:
        print(lst[i], ":", db, "alkalommal szerepel")
