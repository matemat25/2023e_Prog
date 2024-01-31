import random
print("=================== 1. Feladat ===================")
n = int(input("cellák száma: "))
lst = [0]*n
print(lst)
for i in range(1,n-1):
    for j in range(i-1, n, i):
        if(lst[j] == 0):
            lst[j] = 1
        else:
            lst[j] = 0
    print(lst)

print(lst)
for i in range(n):
    if lst[i] == 1:
        print(i+1, end = " ")

print("\n=================== 2. Feladat ===================")

lst2 = []
n = 5
for i in range(n):
    l2 = []
    for j in range (n):
        l2.append(random.randint(1,50))
    lst2.append(l2)
print(lst2)
for i in range(n):
    for j in range(n):
        print(lst2[i][j], end = " ")
    print()

print("\n=================== 3. Feladat ===================")

lst3 = [[0]*9 for i in range(9)]
print(lst3)
n = 5
for i in range(n):
    l3 = []
    for j in range (n):
        lst3[i][j] = random.randint(1, 50)
print(lst3)
n = 9
for i in range(n):
    for j in range(n):
        print("%4i" %lst3[i][j], end = " ")
    print()

print("--- Összegek soronként ---")

for i in range(5):
    s = 0
    for j in range(5):
        s += lst3 [i][j]
    lst3[i][5] = s
n = 9
for i in range(n):
    for j in range(n):
        print("%4i" %lst3[i][j], end = " ")
    print()

print("--- Minimum soronként ---")
for i in range(5):
    minn = float('inf')
    for j in range(5):
        if lst3[i][j] < minn:
            minn = lst3[i][j]
    lst3[i][6] = s
n = 9
for i in range(n):
    for j in range(n):
        print("%4i" %lst3[i][j], end = " ")
    print()

