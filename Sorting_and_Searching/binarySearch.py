#search for sorted alist
#對半撕電話簿找頁碼XD
def binarySearch(alist, item):
    if len(alist) == 0:
        return False
    mid_num = len(alist) // 2
    if alist[mid_num] == item:
        return True
    else:
        if alist[mid_num] > item:
            return binarySearch(alist[mid_num+1:], item)
        else:
            return binarySearch(alist[:mid_num], item)