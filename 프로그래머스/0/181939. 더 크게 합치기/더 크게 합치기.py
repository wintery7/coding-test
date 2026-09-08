def solution(a, b):
    tmp1 = str(a) + str(b)
    tmp2 = str(b) + str(a)
    return int(tmp1 if tmp1 > tmp2 else tmp2)