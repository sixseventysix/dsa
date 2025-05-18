for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    zero_count = 0
    consec_zeroes = 0

    if a[0] == 0:
        zero_count += 1
    for i in range(1, n):
        if a[i] == 0:
            zero_count += 1
        if a[i] == 0 and a[i - 1] == 0:
            consec_zeroes = 1

    
    if consec_zeroes == 1 or zero_count == 0:
        print("yes")
    else:
        print("no")
