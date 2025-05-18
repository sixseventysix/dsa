# even k cannot be an ideal generator, odd k is always an ideal generator
for _ in range(int(input())):
    k = int(input())

    if k % 2 == 0:
        print("no")
    else:
        print("yes")