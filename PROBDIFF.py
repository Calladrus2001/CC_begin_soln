t = int(input())
for _ in range(t):
    a = list(map(int, input().split()))
    b = []
    c = {}
    for x in a:
        c[x] = c.get(x,0) + 1
        if x not in b:
            b.append(x)
    if len(b) == 4:
        print(2)
    elif len(b) == 3:
        print(2)
    elif len(b) == 2:
        for x in c:
            if (c[x] == 3):
                print(1)
                break
            elif (c[x] == 2):
                print(2)
                break
    else:
        print(0)
