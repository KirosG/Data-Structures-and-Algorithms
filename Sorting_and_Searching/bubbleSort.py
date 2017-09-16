import random

def makeList(n,l):
    alist = []
    for i in range(l):
        alist.append(random.randint(1,n))
    return alist

def bubbleSort(alist):
    for sortnum in range(len(alist)-1,0,-1):
        for pos in range(sortnum):
            if alist[pos] > alist[pos+1]:
                temp = alist[pos]
                alist[pos] = alist[pos+1]
                alist[pos+1] = temp
    return alist

def shortBubbleSort(alist):
    sortnum = len(alist) - 1
    exchanges = True
    while sortnum > 0 and exchanges:
        exchanges = False
        for pos in range(sortnum):
            if alist[pos] > alist[pos+1]:
                temp = alist[pos]
                alist[pos] = alist[pos+1]
                alist[pos+1] = temp
                exchanges = True
        sortnum = sortnum - 1
    return alist

alist = makeList(100,20)
a = bubbleSort(alist)
b = shortBubbleSort(alist)
print(a)
print(b)
print(alist)