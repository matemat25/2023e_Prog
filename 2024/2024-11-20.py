l = [1,2,3,4,5]
def összeg(lista):
    s=0
    for i in range(len(lista)):
        s+=lista[i]
    return s

print(összeg(l))

def szorzat(lista):
    s=lista[0]
    for i in range(1,len(lista)):
        s*=lista[i]
    return s

print(szorzat(l))

def osszegzes(lista, f):
    s=lista[0]
    for i in range(1,len(lista)):
        s=f(s,lista[i])
    return s

def osszead(x,y):
    return x+y

print(osszegzes(l, osszead))

def szorzas(x,y):
    return x*y

print(osszegzes(l, szorzas))

x =lambda szam1, szam2 : szam1+szam2

print(x(2,3))

print(osszegzes(l,lambda n,m:n*m))

def maxkivalasztas(lista):
    maxertek=lista[0]
    maxindex=0
    for i in range(1,len(lista)):
        if lista[i]>maxertek:
            maxertek=lista[i]
            maxindex=i
    return (maxindex, maxertek)

l2 = [2,6,5,9,3]
print(maxkivalasztas(l2))

def minkivalasztas(lista):
    minertek=lista[0]
    minindex=0
    for i in range(1,len(lista)):
        if lista[i]<minertek:
            minertek=lista[i]
            minindex=i
    return (minindex, minertek)

print(minkivalasztas(l2))

def szelsoertekkivalasztas(lista:list,f:function)->tuple[int,int]:
    """_summary_

    Args:
        lista (list): _description_
        f (function): _description_

    Returns:
        tuple[int,int]: _description_
    """
    ertek=lista[0]
    index=0
    for i in range(1,len(lista)):
        if f(lista[i],ertek):
            ertek=lista[i]
            index=i
    return (index, ertek)

def min(szam1, szam2):
    return szam1<szam2

print(szelsoertekkivalasztas(l2,min))

def max(szam1, szam2):
    return szam1>szam2

print(szelsoertekkivalasztas(l2,max))

print(szelsoertekkivalasztas(l2,lambda n1, n2:n1<n2))#min
print(szelsoertekkivalasztas(l2,lambda n1, n2:n1>n2))#max
