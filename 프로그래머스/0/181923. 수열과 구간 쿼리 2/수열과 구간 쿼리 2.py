def solution(arr, queries):
    answer = []
    for query in queries:
        s = query[0]
        e = query[1]
        k = query[2]
        smallest_num_bigger_than_k = -1

        for i in range(s,e+1):
            if arr[i] > k and (smallest_num_bigger_than_k > arr[i] or smallest_num_bigger_than_k == -1) :
                smallest_num_bigger_than_k = arr[i]

        answer.append(smallest_num_bigger_than_k)

    if len(answer) == 0:
        return -1

    return answer

print(solution([0, 1, 2, 4, 3], [[0, 4, 2], [0, 3, 2], [0, 2, 2]]))