def solution(video_len, pos, op_start, op_end, commands):
    pos_mm, pos_ss = map(int,pos.split(":"))
    op_start_mm, op_start_ss = map(int, op_start.split(":"))
    op_end_mm, op_end_ss = map(int, op_end.split(":"))
    video_len_mm, video_len_ss = map(int, video_len.split(":"))

    for command in commands:
        if (op_start_mm < pos_mm or (op_start_mm == pos_mm and op_start_ss <= pos_ss)) and (pos_mm < op_end_mm or (pos_mm == op_end_mm and pos_ss < op_end_ss)):
            pos_mm = op_end_mm
            pos_ss = op_end_ss

        if command == "prev":
            pos_ss -= 10
            if pos_mm == 0 and pos_ss < 10:
                pos_ss = 0
            if pos_ss < 0:
                pos_ss += 60
                pos_mm -= 1
            
        elif command =="next":
            pos_ss += 10
            if pos_ss >= 60:
                pos_ss %= 60
                pos_mm += 1    

            if (pos_mm > video_len_mm) or (pos_mm == video_len_mm and pos_ss > video_len_ss):
                pos_mm = video_len_mm
                pos_ss = video_len_ss

        if (op_start_mm < pos_mm or (op_start_mm == pos_mm and op_start_ss <= pos_ss)) and (pos_mm < op_end_mm or (pos_mm == op_end_mm and pos_ss < op_end_ss)):
            pos_mm = op_end_mm
            pos_ss = op_end_ss


    # 정답을 str로 변환

    answer = ""

    if pos_mm < 10:
        answer += "0" + str(pos_mm) + ":"
    else:
        answer += str(pos_mm) + ":"

    if pos_ss < 10:
        answer += "0" + str(pos_ss)
    else:
        answer += str(pos_ss)
    
    return answer