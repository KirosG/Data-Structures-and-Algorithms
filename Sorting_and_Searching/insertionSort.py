import random

def makeList(n,l):
    alist = []
    for i in range(l):
        alist.append(random.randint(1,n))
    return alist

def insertionSort(alist):
    for i in range(1, len(alist)):
        insertnum = alist[i]
        position = i
        while position > 0 and alist[position-1] > insertnum:
            position = position - 1
        alist.pop(i)
        alist.insert(position,insertnum)
    return alist

alist = makeList(100,30)
print(alist)
a = insertionSort(alist)
print(alist)
print(a)

