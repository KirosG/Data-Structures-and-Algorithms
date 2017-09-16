import random

def makeList(n,l):
    alist = []
    for i in range(l):
        alist.append(random.randint(1,n))
    return alist


def shellSort(alist):
    gap = len(alist) // 2
    while gap > 0:
        for start in range(gap):
            gapInsertionSort(alist, start, gap)
        print("After increments of size", gap,"The list is", alist)
        gap = gap // 2
    return alist

# 把數列每n個間隔之數字挑出並做insertionSort排序
def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currentvalue


alist = makeList(100,20)
print(alist)
a = shellSort(alist)
print(alist)
print(a)