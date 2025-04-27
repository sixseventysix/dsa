t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    answer = []
    val = 0
    for _x in range(x):
        print(_x, end = " ")
    for x_ in range(x+1,n):
        print(x_, end = " ")
    print(x)