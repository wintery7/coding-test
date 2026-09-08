def solution(l, r):
    answer =[]
    n = ["0", "5"]

    for a in n:
        for b in n:
            for c in n:
                for d in n:
                    for e in n:
                        for f in n:
                            string = a+b+c+d+e+f
                            if l <= int(string) <= r:
                                answer.append(int(string))

    if len(answer) == 0: return [-1]
    
    return answer