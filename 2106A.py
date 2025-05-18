for _ in range(int(input())):
    n = int(input())
    s = input()

    num_zeroes = s.count('0')
    num_ones = n - num_zeroes

    print(num_ones*n + num_zeroes - num_ones)