def solution(num_list):
    even_number = ''
    odd_number = ''
    for num in num_list:
        if num % 2 == 0 :
            even_number+=str(num)
        else:
            odd_number += str(num)


    answer = int(even_number) + int(odd_number)
    return answer