import hashlib

hash_table = list([0 for i in range(8)]) # 해쉬 테이블 공간 생성

def get_key(data):   # SHA-256 안전한 해쉬 알고리즘으로 해쉬 키 생성, 고정된 크기의 유일한 해쉬 값을 생성해줌
    hash_object = hashlib.sha256()  ## 해쉬 객체 생성
    hash_object.update(data.encode())
    hex_dig = hash_object.hexdigest()
    return int(hex_dig, 16)

def hash_function(key):  # Division을 이용한 간단한 해쉬 함수
    return key % 8


