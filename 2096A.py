for _ in range(int(input())):
    n = int(input())
    a = input()
    iter_s = 1
    iter_e = n
    res = [0] * n
    for i in range(n-2, -1, -1):
        if a[i] == '<':
            res[i+1] = iter_s
            iter_s += 1
        else:
            res[i+1] = iter_e
            iter_e -= 1
    
    res[0] = iter_s   
    print(*res)
