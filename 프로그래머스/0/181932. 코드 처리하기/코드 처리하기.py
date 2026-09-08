def solution(code):
    mode = 0
    answer = ''
    for index, char in enumerate(code):
        if not mode:# mode가 0일 때
            if char != "1" and index % 2 == 0: # 1이 아니고 index가 짝수일 때
                answer += char
            elif char == "1":
                mode = 1
        else: # mode가 1일 때
            if char!= "1" and index % 2 == 1: # 1이 아니고 index가 홀수일 경우
                answer += char
            elif char == "1":
                mode = 0

    if answer == '':
            return "EMPTY"
    return answer