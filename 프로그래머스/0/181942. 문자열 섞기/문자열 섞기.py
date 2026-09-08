def solution(str1, str2):
    answer = ''
    for (str1, str2) in zip(str1, str2):
        answer += str1
        answer += str2
    return answer

print(solution("aaa","bbb"))