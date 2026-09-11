def solution(rank, attendance):
    students = [(r, i) for i, (r, a) in enumerate(zip(rank, attendance)) if a]
    students.sort()

    return students[0][1] * 10000 + students[1][1] * 100 + students[2][1]