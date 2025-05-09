# order of elements in between l and r, before l, after r is going to be same so their cost is the same too
# this means we only care about aligning l & l-1 and r & r+1
# maximum saving on cost is 2 if both l and r are properly aligned
for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    num_changes = 0
    for i in range(n-1):
        if s[i] != s[i+1]: num_changes += 1
    # if s is just 1s or just 0s, cost will be number of characters. 
    # if s is just 1s, then we have to add 1 to account for switch from initial 0 -> 1
    if num_changes == 0:
        print(n + int(s[0] == "1"))
    # one extra cost for the switching
    elif num_changes == 1:
        print(n + int(s[0] == "1") + 1)
    # num_changes >= 2
    else:
        # when num_changes = 2, we rely on the corner elements to get total typing cost 
        # as 1 less than the original cost
        # when it is greater than 2, we can satisfy the condition:
        # s[l-1] != s[l] and s[r] != s[r+1]
        # which gives the final cost as 2 less than the original cost 
        # (only if string starts with a 0 or else we pay a penalty at the start)
        print(n+num_changes -1 - int(s[0] == "0" and num_changes > 2))