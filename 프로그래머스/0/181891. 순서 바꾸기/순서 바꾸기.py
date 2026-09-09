def solution(num_list, n):
    answer = num_list[n:]
    for value in num_list[:n]:
        answer.append(value)
    return answer