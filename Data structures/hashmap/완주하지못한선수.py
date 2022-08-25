def solution(participant, completion):
    partList = {}

    for name in participant:
        if name in partList:
            partList[name] += 1
        else:
            partList[name] = 1

    for finisher in completion:
        if finisher in partList:
            partList[finisher] -= 1
        
    for finisher in partList:
        if partList[finisher] == 1:
            return finisher
    return False
    
# 다른 풀이 1
from collections import Counter

def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]

# 다른 풀이 2 파이썬 내장함수 hash()를 사용하면 특정 key에 대한 해쉬키를 생성할 수 있음. - 수의 가감을 이용한 풀이
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part  # 각 참가자 이름에 대한 고유한 해쉬 키를 저장
        temp += int(hash(part)) # 각 참가자 별 해쉬키 값을 다 저장함
    for com in completion:
        temp -= hash(com) # 각 완주자 별 해쉬키 값을 다시 뺌
    answer = dic[temp] # 빼고 남은 값이 완주하지 못한 나머지 한명에 대한 해쉬 키 값임

    return answer