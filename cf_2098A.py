t = int(input())
for _ in range(t):
    s = input()
    count = [0] * 10
    for ch in s:
        count[int(ch)] += 1

    answer = []
    for i in range(10):
        lower_bound = 10 - i - 1  # since i is 0-based
        for d in range(lower_bound, 10):
            if count[d] > 0:
                answer.append(str(d))
                count[d] -= 1
                break
            print(''.join(answer))
