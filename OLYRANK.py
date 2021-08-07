t = int(input())
for x in range(t):
    a = list(map(int, input().split()))
    c1 = a[:3]
    c2 = a[3:]
    if sum(c1) > sum(c2):
        print(1)
    else:
        print(2)
