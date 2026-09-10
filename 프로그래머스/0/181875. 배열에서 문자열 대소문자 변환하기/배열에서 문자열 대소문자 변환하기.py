def solution(strArr):
    answer = list(strArr)
    for i, char in enumerate(answer):
        if i % 2 == 0:
            answer[i] = char.lower()
        else:
            answer[i] = char.upper()
    return answer