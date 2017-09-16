import random

def makeList(n,l):
    alist = []
    for i in range(l):
        alist.append(random.randint(1,n))
    return alist

def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)
    return alist

def quickSortHelper(alist,first,last):
    if first<last:
        splitpoint = partition(alist,first,last)

        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)

#把數列大於pivotvalue放右邊,小於pivotvalue放左邊
def partition(alist,first,last):
    pivotvalue = alist[first]

    leftmark = first+1
    rightmark = last
    done = False
    while not done:
        #往右掃描 找到比pivotvalue大或等於的停住
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
        #往左掃描 找到比pivotvalue小或等於的停住
        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1
        #如果兩邊指針交叉了就停
        if rightmark < leftmark:
            done = True
        #左右邊交換
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp
    #把pivotvalue換過去右邊指針,因為最後左邊跟右邊指針會交叉,
    #分別停在pivot點的右邊(左邊指針)跟左邊(右邊指針),然後要交換右邊指針上的數字,因為那邊小於pivotvalue
    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark

alist = makeList(100,20)
print(alist)
a = quickSort(alist)
print(alist)
print(a)