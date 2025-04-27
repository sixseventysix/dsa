import sys
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_max = max(a)
    a_min = min(a)
    if all(_b == -1 for _b in b):
        print(k-(a_max - a_min - 1))
    else:
        s = None
        found = False

        for i in range(len(b)):
            if b[i] != -1:
                if not found:
                    s = a[i] + b[i]
                    found = True
                else:
                    if a[i] + b[i] != s:
                        print(0)
                        break
        if s < a_max or s > (a_min + k):
            print(0)
        else:
            print(1)

