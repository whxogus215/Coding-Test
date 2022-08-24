# open hashing
# https://idm101.tistory.com/3
class OpenHash:
    def __init__(self, table_size):
        self.size = table_size
        self.hash_table = [ 0 for a in range(self.size)]
    
    def getKey(self, data):
        self.key = ord(data[0])
        return self.key
    
    def hashFunction(self, key):
        return key % self.size
    
    def getAddress(self, key):
        myKey = self.getKey(key)
        hash_address = self.hashFunction(myKey)
        return hash_address
    
    def save(self, key, value):
        hash_address = self.getAddress(key)

        # 해당 공간에 데이터가 이미 있을 때 (Collision)
        if self.hash_table[hash_address] != 0:
            for index in range(len(self.hash_table[hash_address])):
                # 해당 공간에 연결리스트로 접근
                if self.hash_table[hash_address][index][0] == key:
                    self.hash_table[hash_address][index][1] = value
                    return # 밑 코드는 읽지 않고 건너뜀
            # key가 다르면 key와 value를 쌍으로 같이 저장 (linked list에 추가)
            self.hash_table[hash_address].append([key, value])
        else:
            self.hash_table[hash_address] = [[key, value]]

    def read(self, key):
        hash_address = self.getAddress(key)

        if self.hash_table[hash_address] != 0:
            for index in range(len(self.hash_table[hash_address])):
                if self.hash_table[hash_address][index][0] == key:
                    return self.hash_table[hash_address][index][1]
            return False
        else:
            return False

    def delete(self, key):
        hash_address = self.getAddress(key)

        if self.hash_table[hash_address] != 0:
            # 값이 두개 이상일 경우 key와 value를 비교
            for index in range(len(self.hash_table[hash_address])):
                if self.hash_table[hash_address][index][0] == key:
                    if len(self.hash_table[hash_address]) == 1: # 데이터 개수가 1개일 때
                        self.hash_table[hash_address] = 0
                    else : # 데이터 개수가 2개 이상일 때
                        del self.hash_table[hash_address][index]
                    return
            return False
        else :
            return False

#Test Code
h_table = OpenHash(8)

h_table.save('aa', '1111')
h_table.read('aa')

data1 = 'aa'
data2 = 'ad'

print(ord(data1[0]))
print(ord(data2[0]))

h_table.save('ad', '2222')
print(h_table.hash_table)

print(h_table.read('aa'))
print(h_table.read('ad'))

h_table.delete('aa')
print(h_table.hash_table)
print(h_table.delete('Data'))
h_table.delete('ad')
print(h_table.hash_table)

