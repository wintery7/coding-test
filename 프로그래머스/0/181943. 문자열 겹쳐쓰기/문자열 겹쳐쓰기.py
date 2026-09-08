def solution(my_string, overwrite_string, s):
    answer = my_string[:s]
    answer += overwrite_string
    answer += my_string[len(overwrite_string)+s:]
    
    return answer

print(solution("He11oWor1d","lloWorl",2 ))