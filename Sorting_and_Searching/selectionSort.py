import random

def makeList(n,l):
    alist = []
    for i in range(l):
        alist.append(random.randint(1,n))
    return alist

def selectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax=0
        for location in range(1,fillslot+1):
            if alist[location]>alist[positionOfMax]:
                positionOfMax = location

        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp
    return alist

alist = makeList(100,20)
print(alist)
a = selectionSort(alist)
print(alist)
print(a)
