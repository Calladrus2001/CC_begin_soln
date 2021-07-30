t = int(input())
for x in range(t):
    d, x, y, z = map(int, input().split())
    w1 = 7*x
    w2 = d*y + (7-d)*z
    print(max(w1, w2))
