import random

# Üres lista létrehozása
szamok = []

# Feladat 1: Véletlen számok listába töltése
print("======= 1. Feladat =======")
for _ in range(20):
    szam = random.randint(1,120)
    if szam not in szamok:   
        szamok.append(szam)

print(szamok)

# Feladat 2: Páros és páratlan számok megszámlálása
print("======= 2. Feladat =======")
paros_25_felett = 0
paratlan_25_alatt = 0

for szam in szamok:
    if szam % 2 == 0 and szam > 25:
        paros_25_felett += 1
    elif szam % 2 != 0 and szam < 25:
        paratlan_25_alatt += 1

print("Páros számok száma > 25: ", paros_25_felett)
print("Páratlan számok száma < 25: ", paratlan_25_alatt)

# Feladat 3: Páros számok átlagának kiszámítása
print("======= 3. Feladat =======")
osszeg = 0
db = 0

for szam in szamok:
    if szam % 2 == 0:
        osszeg += szam
        db += 1
atlag = osszeg / db
print("Páros számok átlaga:",atlag)

# Feladat 4: 25-nél kisebb páratlan számok visszafelé kiírása
print("======= 4. Feladat =======")
i = 0
for i in range(len(szamok)-1, -1, -1):
    if szamok[i] < 25 and szamok[i] % 2 != 0:
        print(szamok[i], end = ", ")

# Feladat 5: Páros számok kiírása és megszámlálása, amelyeknek mindkét szomszédja páratlan
print("\n======= 5. Feladat =======")

páros_számok = []
páros_számok_száma = 0

for i in range(1, len(szamok) - 1):
    if szamok[i] % 2 == 0 and szamok[i-1] % 2 != 0 and szamok[i+1] % 2 != 0:
        páros_számok.append(szamok[i])
        páros_számok_száma += 1

print("Páros számok, amelyeknek mindkét szomszédja páratlan:")
for szam in páros_számok:
    print(szam, end = ", ")

print("\nA fenti feltételnek megfelelő páros számok száma: ", páros_számok_száma)

# Feladat 6: Szám párosok keresése, amelyek összege < 100
print("======= 6. Feladat =======")
for i in range(len(szamok)):
    for j in range(i+1, len(szamok)):
        if szamok[i] % 2 == 0 and szamok[j] % 2 == 0:
            osszeg = szamok[i] + szamok[j]
            if osszeg < 100:
                print(i, j)

