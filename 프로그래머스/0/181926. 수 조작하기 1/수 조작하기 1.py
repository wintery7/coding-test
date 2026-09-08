def solution(n, control):
    for task in control:
        if task == "w":
            n += 1
        elif task == "s":
            n -= 1
        elif task == "a":
            n -= 10
        elif task == "d":
            n += 10

    return n