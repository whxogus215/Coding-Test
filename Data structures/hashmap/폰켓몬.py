from typing import Counter

def solution(nums):
    # 폰켓몬 번호의 종류 개수를 해쉬맵 Counter 객체로 받는다.
    dic = Counter(nums)
    max_count = int(len(nums)/2)
    # 종류 갯수 = len(dic)
    # 최대값을 구한다는 것은 그 객체에 담긴 요소의 종류 가짓수만 체크하고, 그것이 뽑아야 하는 개수랑 비교만 하면 된다.

    if len(dic) <= max_count:
        answer = len(dic)
    else :
        answer = max_count

    return answer

# 다른사람 풀이 (Counter 사용 안함)
# 종류 갯수만 구하는 경우기 때문에 중복을 허용하지 않는 set 함수를 사용할 수 있음.
def solution2(nums):
    return min(len(nums)/2, len(set(nums)))