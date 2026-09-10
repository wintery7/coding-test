def solution(myString, pat):
    answer = ''
    return myString[:myString.rfind(pat)+len(pat)]