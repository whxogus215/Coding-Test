# F(Key) -> HashCode -> Index -> Value
#  Key = String, Number, FIle 
# 배열의 해당 인덱스에 접근하기 위해서 O(1)의 장점을 이용하는 방법인 HashTable 임
# 해쉬란 입력된 값을 해쉬 함수를 통해 특정 숫자로 변환한 결과물
# https://jinyes-tistory.tistory.com/10

# 해쉬테이블의 핵심 : 고정된 배열을 선언(데이터 담을 공간), Key를 변환하는 해쉬 함수
from operator import truediv


class HashTable:
    def __init__(self, table_size):
        self.size = table_size
        self.hash_table = [0 for a in range(self.size)]
    
    def getKey(self, data):
        self.key = ord(data[0])
        return self.key

    def hashFunction(self, key):
        return key % self.size
    
    # getKey + hashFunction
    def getAddress(self, key):
        myKey = self.getKey(key)
        hash_address = self.hashFunction(myKey)
        return hash_address
    
    def save(self, key, value):
        hash_address = self.getAddress(key)
        self.hash_table[hash_address] = value
        
    def read(self, key):
        # 1. 키를 해쉬함수를 통해서 해쉬로 변환한다.
        hash_address = self.getAddress(key)
        # 2. 변환한 해쉬로 인덱스를 구해서 해당 인덱스에 접근한다.
        return self.hash_table[hash_address]

    def delete(self, key):
        hash_address = self.getAddress(key)
        
        if self.hash_table[hash_address] != 0:
            self.hash_table[hash_address] = 0
            return True  # return 문을 만나면 함수가 종료 됨
        else :
            return False

# Test Code
h_table = HashTable(8)
h_table.save('a','1111')
h_table.save('b','3333')
h_table.save('c','5555')
h_table.save('d','8888')

print(h_table.hash_table)
print(h_table.read('d'))

print(h_table.delete('d'))