t = int(input())
for x in range(t):
    s = list(map(int, input().split()))
    if (0 in s) & (1 in s):
        print(1)
    else:
        print(0)
