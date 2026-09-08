from math import prod

def solution(num_list):
    multiply = prod(num_list)
    square_sum = sum(num_list)**2

    answer = 0
    if square_sum > multiply:
        answer = 1
    return answer