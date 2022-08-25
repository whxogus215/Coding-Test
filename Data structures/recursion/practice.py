# recursion은 함수가 똑같은 것이 여러번 반복되기 때문에 값이 커지면 실행 시간이 매우 길어짐
# 따라서 메모화라는 과정을 거쳐서 문제를 해결할 수 있음.

# Recursion 핵심 : base case (빠져나올 수 있는 조건), recursive case (재귀함수 호출하는 조건) 이 두 가지가 반드시 있어야 한다.
# 재귀함수는 매개변수를 통해서 Base Condition 에 점차 다가가도록 설계하는 것이 원칙이다. 그래야 재귀함수를 안전하게 종료시킬 수 있기 때문이다.

# 참고 자료 : https://velog.io/@newon-seoul/%EB%AC%B8%EA%B3%BC%EC%83%9D%EC%9D%B4-%EC%A0%81%EC%96%B4%EB%B3%B4%EB%8A%94-%EB%B0%B1%ED%8A%B8%EB%9E%98%ED%82%B9-%EC%9E%AC%EA%B7%80%EC%99%80-DFS-%EB%A5%BC-%EA%B3%81%EB%93%A4%EC%9D%B8
# 재귀 함수 이해 : https://www.secmem.org/blog/2021/07/09/recursion/
# 재귀 함수 이해 : https://targetcoders.com/%EC%9E%AC%EA%B7%80%ED%95%A8%EC%88%98-%EC%98%88%EC%A0%9C-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0/


메모 = {
    1 : 1, # 피보나치 수열 f(1) = 1  
    2 : 1  # f(2) = 1
}

def f(n):
    # 조기 리턴 방식, 조건에 맞으면 바로 함수에서 벗어나는 방식 - if-else 문을 사용 X
    if n in 메모:
        return 메모[n]
    output = f(n-1) + f(n-2)
    메모[n] = output # 결과 값을 리턴하기 전에 한번 메모리에 저장함
    return output


"""
재귀함수는 컴퓨터에 선언하는 프로그래밍 방식이기 때문에 모든 로직을 다 이해할 필요는 없다.
다만 base case와 recursive case를 명확히 작성해야 한다.

즉, 재귀함수 간의 관계(like 점화식)를 정확하게 작성하고, base case를 작성하면 그 안의 세부적인 코드가 돌아가는 내용은
신경쓰지 않아도 된다는 뜻이다.

딱 두 가지만 알자. base case 그리고 recursive case

Tip : 변수가 정방향인지 역방향인지를 이해하기!

기본 구조

함수:
if - base case

recursive case

"""