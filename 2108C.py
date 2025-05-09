from itertools import groupby

# grouping adjacent values which are equal because one clone can travel to all those spots (no need for another clone)
# new clone will be required for each local maxima as to reach a local maxima from somewhere else, we will visit
# a smaller element which means we will press the buttons in an inappropriate order
# from local maximas, clones can move freely and press buttons in the right order
# adding a large negative integer on both sides of the list so that first and last element are also counted as a local maxima
# if they are larger than their immediate neighbouring value
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    filtered = [key for key, _ in groupby(a)]
    filtered = [-10**9] + filtered + [-10**9]
    ans = 0
    for i in range(1, len(filtered)-1):
        if filtered[i] > filtered[i-1] and filtered[i] > filtered[i+1]:
            ans+=1
    print(ans)