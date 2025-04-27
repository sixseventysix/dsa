t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    answer = []
    val = 0
    for _ in range(n):
        if(val == x):
            val+=1
            continue
        answer.append(val)
        val+=1
    answer.append(x)
    print(*answer)