# correct but TLE

t = int(input())
for x in range(t):
    n, m = map(int, input().split())
    c = list(map(int, input().split()))
    r = list(map(int, input().split()))
    p = []
    for x in range(m):
        p1 = list(map(int, input().split()))
        p1.pop(0)
        p.append(p1)
        p1 = []
    st_r = 1
    trip = 0
    for x in range(r[0]):
        a = r.index(st_r)
        rank = []
        for y in p[a]:
            if c[y-1] != 1000:
                rank.append(c[y-1])
        if len(rank) != 0:
            mini = min(rank)
            if x == r[0] - 1:
                trip = 1
                print(c.index(mini) + 1)
            c[c.index(mini)] = 1000
            st_r += 1
    if (trip == 0):
        print(0)
