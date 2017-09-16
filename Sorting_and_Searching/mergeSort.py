import random

def makeList(n,l):
    alist = []
    for i in range(l):
        alist.append(random.randint(1,n))
    return alist

def mergeSort(alist):
    print("Splitting ", alist)
    if len(alist) > 1:
        mid = len(alist)//2
        leftside = alist[:mid]
        rightside = alist[mid:]

        mergeSort(leftside)
        mergeSort(rightside)

        i,j,k = 0,0,0

        while i < len(leftside) and j < len(rightside):
            if leftside[i] > rightside[j]:
                alist[k] = rightside[j]
                j = j+1
                k = k + 1
            else:
                alist[k] = leftside[i]
                i = i+1
                k = k + 1

        while i < len(leftside):
            alist[k] = leftside[i]
            i = i + 1
            k = k + 1

        while j < len(rightside):
            alist[k] = rightside[j]
            j = j + 1
            k = k + 1
    print("merge",alist)

alist = makeList(100,10)
mergeSort(alist)
