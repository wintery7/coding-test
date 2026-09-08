def solution(arr, queries):
    for query in queries:
        prev = query[0]
        next = query[1]

        tmp = arr[prev]
        arr[prev] = arr[next]
        arr[next] = tmp

    return arr