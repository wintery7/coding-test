def solution(myString, pat):
    answer = 0
    list_myString = list(myString)
    for i, c in enumerate(list_myString):
        if c == "A":
            list_myString[i] = "B"
        elif c == "B":
            list_myString[i] = "A"

    if pat in "".join(list_myString):
        return 1

    return answer