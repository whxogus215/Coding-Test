# close hashing
# https://jinyes-tistory.tistory.com/12?category=841411
class CloseHash:
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

        if self.hash_table[hash_address] != 0:
            # 해당 인덱스부터 마지막까지 하나씩 내려가면서 빈 공간을 찾음
            for index in range(hash_address, len(self.hash_table)):
                if self.hash_table[index] == 0: # for문으로 하나씩 내려가다가 빈공간이 있을 때
                    self.hash_table[index] = [key, value]
                    return
                elif self.hash_table[index][0] == key: # key가 같으면 덮어쓰기
                    self.hash_table[index][1] = value
                    return
            '''
            두 코드를 바꿔서 작성했을 때 TypeError: 'int' object is not subscriptable가 생기는 이유
            if self.hash_table[index][0] == key: 
                    self.hash_table[index][1] = value
                    return
            elif self.hash_table[index] == 0: 
                    self.hash_table[index] = [key, value]
                    return
            return None

            파이썬은 위에서 부터 한줄씩 내려가면서 읽는다. 따라서 빈 공간에 데이터를 저장하려고 해도
            if self.hash_table[index][0] == key: 이부분에서 self.hash_table[index][0]은 현재 0인 int 타입이고
            key는 string이기 때문에 서로 타입이 맞지 않아 오류가 생긴다.
            두 개를 다시 바꿔서 작성하면 오류가 날 수 있는 코드가 실행되기 전에 함수가 종료되기 때문에 오류가 발생하지 않는다.
            '''
        else: # collision이 없을 때, 그냥 넣기
            self.hash_table[hash_address] = [key, value]

    def read(self, key):
        hash_address = self.getAddress(key)

        for index in range(hash_address, len(self.hash_table)):
            if self.hash_table[index][0] == key:
                return self.hash_table[index][1]
        return None

    def delete(self, key):
        hash_address = self.getAddress(key)

        for index in range(hash_address, len(self.hash_table)):
            if self.hash_table[index] == 0:
                continue # continue를 쓰는 이유 : 찾는 key가 나올 때까지 주소를 내리는 것이므로 key가 안나오면 바로 index 값을 1 올려야 됨. 밑에 if문은 확인할 필요도 없음.
            if self.hash_table[index][0] == key:
                self.hash_table[index] = 0
                return
        return False # 찾는 값이 없을 경우 False 반환

#Test Code
h_table = CloseHash(8)

data1 = 'aa'
data2 = 'ad'
print(ord(data1[0]), ord(data2[0]))

h_table.save('aa', '3333')
h_table.save('ad', '9999')
print(h_table.hash_table)

h_table.read('ad')

h_table.delete('aa')
print(h_table.hash_table)

h_table.delete('ad')
print(h_table.hash_table)

