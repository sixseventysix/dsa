for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    max_idx = a.index(max(a))
    if all(x == a[0] for x in a):
        print("no")
    else:
        print("yes")
        b = [1] * n
        b[max_idx] = 2
        print(*b)

         

    