def solution(a, b):
    answer = []
    carry = 0

    a = a[::-1]
    b = b[::-1]

    for i in range(max(len(a), len(b))):
        x = int(a[i]) if i < len(a) else 0
        y = int(b[i]) if i < len(b) else 0

        total = x + y + carry
        answer.append(str(total % 10))
        carry = total // 10

    if carry:
        answer.append(str(carry))

    return ''.join(answer[::-1])