import random

'''
1; tölts fel egy listát véletlen számokkal
2; hány darab páros ill. páratlan szám van
3; számold ki a számok összegét
4; számold ki a páros illetve a páratlan számok összegét
5; számold ki minden 3-ik szám összegét
6; számold ki hármassával a számok összegeit
7; irasd ki visszafelé minden 2. számot
'''
dbs = 0
db = 0
i = 0
n = 20
lst = []


for i in range(n):
    r = random.randint(1,50)
    lst.append(r)
print(lst)
print("\n 2, 3. Feladat------------------------------------------------------------")
for i in lst:
    if i % 2 == 0:
        print(i, end = ", ")
        db += 1
    else:
        print(i, end = ", ")
        dbs += 1
print("\nPáratlan db: ", dbs)
print("\nPáros db: ", db)
print("\n 4. Feladat ------------------------------------------------------------")
x = 0 #páros
y = 0 #páratlan
z = 0
for i in lst:
    z+=i
    if i % 2 == 0:
        x += i
    else:
        y += i

print("Páros számok összege:", x)
print("Páratlan számok összege:", y)
print("A számok összege:", z)

print("\n 5. Feladat ------------------------------------------------------------")
osszeg = 0
for i in range(0, n, 3):
    print(i, end = ", ")
    osszeg += lst[i]
print("\nMinden harmadik szm összege:", osszeg)
print("\n6. Feladat ------------------------------------------------------------")
for i in range(0,n-2,3):
    s_3_cs = 0
    print("i: ", i)
    for j in range(3):
        s_3_cs += lst[i+j]
        print("i+j: ", i+j)
    print(s_3_cs)
print("\n7. Feladat ------------------------------------------------------------")
for i in range (n-2, -1, -2):
    print(lst[i], end =", ")









