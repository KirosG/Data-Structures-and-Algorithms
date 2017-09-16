class HashTable():
    def __init__(self):
        self.size = 11 #for hash function and define slots size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == None: #如果slot是空的就直接塞
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else: #發生collision
            if self.slots[hashvalue] == key: #如果put進來這個slot的key跟原本相同就替換data
                self.data[hashvalue] = data  # replace
            else: #如果key不同
                nextslot = self.rehash(hashvalue, len(self.slots)) #重新給hashvalue
                while self.slots[nextslot] != None and self.slots[nextslot] != key: #直到重給的shot是空的或是有相同key為止
                    nextslot = self.rehash(nextslot, len(self.slots))
                if self.slots[nextslot] == None: #空的就插入
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else: #相同就替換data
                    self.data[nextslot] = data  # replace

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots)) #原始key對應進來的slot 開始找
        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:  #直接對應的position就是 找到!
                found = True
                data = self.data[position]
            else: #對應position的key不是 就rehash往旁邊找
                position = self.rehash(position, len(self.slots))
                if position == startslot: #找一圈沒有就表示沒有!
                    stop = True
        return data

    def hashfunction(self, key, size): #餘數法
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash+1) % size

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)

H=HashTable()
H[54]="cat"
H[26]="dog"
H[93]="lion"
H[17]="tiger"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"
print(H.slots)
print(H.data)

print(H[20])

print(H[17])
H[20]='duck'
print(H[20])
print(H[99])