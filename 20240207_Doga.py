import random

#1. Feladat: 25 elemű lista egy 1-50
print("=================== 1. Feladat ===================")
lst = []
for i in range(25):
    n = random.randint(1, 50)
    lst.append(n)
print(lst)
#----------------------------------------------------------------------------------------------------

#2. Feladat: Keresd meg az ismétlődő azámokat és hányszor ismétlődik
print("=================== 2. Feladat ===================")
ismétlődők = []
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] == lst[j] and lst[i] not in ismétlődők:
            ismétlődők.append(lst[i])

# Kiíratás
print("Az ismétlődő számok a listában:")
for num in ismétlődők:
    print(num, end = ", ")

#----------------------------------------------------------------------------------------------------

#3. Feladat: Keresd meg melyik szám nem szerepel a lisitában
print("\n=================== 3. Feladat ===================")
for szam in range(1, 50):
    if szam not in lst:
        print("Az első olyan szám, ami nem szerepel a listában:", szam)


#----------------------------------------------------------------------------------------------------

#4. Feladat: Keresd meg azt a két nem egyenlő számot amelynek az összege a legkisebb
print("\n=================== 4. Feladat ===================")

for i in range(len(lst)-1):
    for j in range(i + 1, len(lst)):



#----------------------------------------------------------------------------------------------------

#5. Feladat: Keresd meg azt a két számot amelynek 2 szomszédja kisebb mint a keresett szám
print("\n=================== 5. Feladat ===================")


for i in range(n-1):
        if lst[i-1] < lst[i] and lst[i] > lst[i+1]:
            print("\n", lst[i-1], lst[i], lst[i+1])

