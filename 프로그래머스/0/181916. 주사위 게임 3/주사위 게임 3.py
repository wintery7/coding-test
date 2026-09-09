def solution(a, b, c, d):
    tmp = [a,b,c,d]
    tmp.sort()
    nums = []
    count = []

    for n in tmp:
        if nums.count(n) == 0:
            nums.append(n)
            count.append(1)
        else:
            count[nums.index(n)] += 1

    p = nums[count.index(max(count))]

    length_of_nums_arr = len(nums)
    max_num_of_count = max(count)

    if max_num_of_count == 4:
        return 1111*p
    elif max_num_of_count == 3:
        q =  nums[count.index(1)]
        return (10*p+q)**2
    elif max_num_of_count == 2 and length_of_nums_arr == 2:
        q = nums[1]
        return (p+q)*(abs(p-q))
    elif max_num_of_count == 2 and length_of_nums_arr == 3:
        q = -1
        r = -1

        for i,value in enumerate(count):
            if value == 1 and q == -1:
                q = nums[i]
            elif value == 1 and q != -1:
                r = nums[i]
        return r*q
    elif max_num_of_count == 1:
        return tmp[0]


    return -1


print(solution(2,2,2,2))