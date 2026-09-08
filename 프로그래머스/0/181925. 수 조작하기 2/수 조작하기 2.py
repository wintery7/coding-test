def solution(numLog):
    answer = ''

    for i in range(len(numLog)-1):
        num_prev = numLog[i]
        num_next = numLog[i+1]
        change_value = num_next - num_prev

        if change_value == 1:
            answer += "w"
        elif change_value == -1:
            answer += "s"
        elif change_value == 10:
            answer += "d"
        elif change_value == -10:
            answer += "a"
         
    return answer