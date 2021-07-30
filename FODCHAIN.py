t = int(input())
for x in range(t):
    e, k = map(int, input().split())
    count = 0
    while e != 0:
        e = e//k
        count += 1
    print(count)
