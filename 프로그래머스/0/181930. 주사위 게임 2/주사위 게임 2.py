def solution(a, b, c):
    answer = 0
    if a.__eq__(b) and a.__eq__(c) and b.__eq__(c): # a b c 모두 같을 때
        answer += (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)
    elif a.__eq__(b) or a.__eq__(c) or b.__eq__(c): # 같은 게 하나라도 있을 때
        answer += (a+b+c)*(a**2+b**2+c**2)
    else: # 모두 다를 때
        answer += (a + b + c)

    return answer
