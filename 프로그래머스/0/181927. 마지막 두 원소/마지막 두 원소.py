def solution(num_list):
    last_number = num_list[len(num_list)-1]
    before_last_number = num_list[len(num_list)-2]
    if last_number > before_last_number:# 마지막 원소가 그 전 원소보다 클 때
        num_list.append(last_number-before_last_number)
    else:# 그렇지 않을때
        num_list.append(last_number*2)
    answer = num_list
    return answer