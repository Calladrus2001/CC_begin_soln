t = int(input())
for x in range(t):
    s = input()
    s1 = []
    for x in s:
        s1.append(x)
    s2 = []
    for x in s1:
        if x not in s2:
            s2.append(x)
    count = []        
    for x in s2:
        c = s1.count(x)
        count.append(c)
    count.sort()
    trip = 0
    for x in range(len(count)-2):
        if count[x] + count[x+1] == count[x+2]:
            pass
        else:
            count[0],count[1] = count[1],count[0]
            if count[x] + count[x+1] == count[x+2]:
                pass
            else:
                trip = 1
    if trip == 0:
        print('Dynamic')
    else:
        print('Not')               