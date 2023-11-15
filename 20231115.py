import random

n = 20
lst = []
for i in range(n):
    r = random.randint(1,50)
    lst.append(r)
print(lst)

y = int(input("Adj meg egy számot: "))

if y in lst:
    print(y, " benne van a listában!")
else:
    print(y, "Nincs benne a listában!")

if y not in lst:
    print(y, "Nincs benne a listában!")
else:
    print(y, " benne van a listában!")

for x in range(1,10):
    db = 0
    for y in lst:
        if x == y:
            db += 1
            if db > 1:
                print(x, end = ", ")
                break
            
         
