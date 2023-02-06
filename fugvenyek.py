#legyen ez a megjegyzés // fügvényekről
def teszt(nev):
    print("Szia "+nev+"!")

teszt("pisti")
teszt("Béla")
teszt("Lajos")
#------------- Matek ----------
def negyzet(x):
    n=x*x
#    print(n)
    return n
negyzet(3)
print(negyzet(3))

harom=negyzet(3)
negy=negyzet(4)
ot=negyzet(5)
print((harom+negy)/ot)


for i in range(1,101):
    x=negyzet(i)
    print(i,"|",x)
print(x)


def kiIr(lista):
    for x in lista:
        print(x,end=",")
    print()
print("-------------")
l = list()
l = [1,2,3]
print(l[1])
print("-------------")

def kiIr2(lista):
    for i in range(len( lista)):
        print(i,lista[i])

en_Listam=(1,2,3,4,2,3)
print(en_Listam)

kiIr(en_Listam)
kiIr2(en_Listam)
en_Listam=[1,2,3,4,2,3]
print(en_Listam)

kiIr(en_Listam)
kiIr2(en_Listam)
en_Listam={1,2,3,4,2,3}
print(en_Listam)

kiIr(en_Listam)
#kiIr2(en_Listam)

#def add(a,b):
#   return a+b

#def add(a,b,c):
#    return a+b+c

def add(a,b,c,d):
    return a+b+c+d


#print(add(1,2))
#print(add(1,2,3))
print(add(1,2,3,4))




def add2(*szam):
    osszeg=0
    for x in szam:
        osszeg+=x
    #print(type(szam))
    return osszeg
print(add2(1))
print(add2(1,2))
print(add2(1,2,3,4,5))