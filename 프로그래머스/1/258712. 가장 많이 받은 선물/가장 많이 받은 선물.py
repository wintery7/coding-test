def solution(friends, gifts):
    # 이번 달선물 지수
    gift_score = [0] * len(friends)
    # 다음 달에 받는 선물의 수
    gift_count = [0] * len(friends)
    # 누가 누구에게 줬는지 체크하기 위한 이차원 배열
    arr = [[0] * len(friends) for _ in range(len(friends))]

    # gifts 를 통해 선물 지수 계산
    for giver, receiver in [gift.split() for gift in gifts]:
        giver_index = friends.index(giver)
        receiver_index = friends.index(receiver)
        arr[giver_index][receiver_index] += 1

        # 기버면 스코어 + 1 리시버 - 1
        for friend in friends:
            if friend == giver:
                gift_score[giver_index] += 1
            elif friend == receiver:
                gift_score[receiver_index] -= 1
            # 누가 누구한테 줬는지 기록

    # 전체 순회하면서 누구에게 선물할지 계산
    for person_index in range(len(friends)-1):
        for give_to_whom_index in range(person_index+1, len(friends)):
            # 자기가 자기한테 주는 경우는 없음으로 제외
            if give_to_whom_index == person_index:
                continue
            # 다른 사람한테 어떻게 줄지 계산
            if arr[person_index][give_to_whom_index] > arr[give_to_whom_index][person_index]:
                gift_count[person_index] += 1
            elif arr[person_index][give_to_whom_index] < arr[give_to_whom_index][person_index]:
                gift_count[give_to_whom_index] += 1
            else:
                # 서로 주고 받은 경우가 없거나 같을 경우 선물지수로 비교
                if gift_score[person_index] > gift_score[give_to_whom_index]:
                    gift_count[person_index] += 1
                elif gift_score[person_index] == gift_score[give_to_whom_index]:
                    continue
                elif gift_score[person_index] < gift_score[give_to_whom_index]:
                    gift_count[give_to_whom_index] += 1


    # 제일 많이 받는 사람의 선물 수 리턴
    answer = max(gift_count)

    return answer

# print(solution(["muzi", "ryan", "frodo", "neo"], ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]))
# print(solution(["joy", "brad", "alessandro", "conan", "david"], ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]))
# print(solution(["a", "b", "c"], ["a b", "b a", "c a", "a c", "a c", "c a"]))