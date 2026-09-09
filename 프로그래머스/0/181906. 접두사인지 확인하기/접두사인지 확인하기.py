def solution(my_string, is_prefix):
    prefix = []
    for i in range(len(my_string)):
        prefix.append(my_string[:len(my_string)-i])

    if is_prefix in prefix:
        return 1
    else:
        return 0