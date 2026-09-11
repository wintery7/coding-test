def solution(arr):
    answer = []
    
    row = len(arr)
    col = len(arr[0]) 

    if row > col:
        for i, r in enumerate(arr):
            for _ in range(row - col):
                arr[i].append(0)
    elif row < col:
        for _ in range(col - row):
            arr.append([0]*col)
    return arr