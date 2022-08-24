from typing import Counter

# 내 풀이
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ranMap = {}
        magMap = {}
        
        for letter in ransomNote:
            if letter in ranMap:
                ranMap[letter]+=1
            else:
                ranMap[letter] = 1

        for letter in magazine:
            if letter in magMap:
                magMap[letter]+=1
            else:
                magMap[letter] = 1
                
        count = len(ransomNote)

        for letter in ransomNote:
            if letter in magMap and magMap[letter] > 0:
                magMap[letter] -= 1
                count -= 1
            if count == 0:
                return True
        return False

        # 다른 사람 풀이 - 위에서 반복문으로 구현한 내용을 Counter 모듈을 사용하면 바로 구현이 가능하다.
        dic = Counter(magazine)
        for char in ransomNote:
            if char not in dic:
                return False
            else:
                dic[char] -= 1
                if dic[char] < 0:
                    return False
        return True