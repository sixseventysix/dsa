for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if (a + b + c)%3 != 0 :
        print("NO")
        continue
    x = (a + b + c) // 3
    if b <= x:
        print("YES")
    else:
        print("NO")
