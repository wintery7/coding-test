def solution(arr):
    n = 1

    while n < len(arr):
        n *= 2

    arr += [0] * (n - len(arr))

    return arr