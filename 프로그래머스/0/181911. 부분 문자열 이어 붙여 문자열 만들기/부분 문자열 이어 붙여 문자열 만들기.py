def solution(my_strings, parts):
    answer = ''
    for my_string, part in zip(my_strings, parts):
        s, e = part
        answer += my_string[s:e+1]

    return answer