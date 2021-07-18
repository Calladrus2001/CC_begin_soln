t = int(input())
for x in range(t):
    n,m = map(int,input().split())
    ja = list(map(int,input().split()))
    jo = list(map(int,input().split()))
    count = 0
    if sum(jo)>sum(ja):
        for _ in range(len(ja)): #because if he swaps all his votes and still cant win, its impossible anyway
            x = max(jo)
            jo.remove(x)
            ja.append(x)
            y = min(ja)
            ja.remove(y)
            jo.append(y)
            count+=1
            if sum(ja)>sum(jo): # for minimum number of swaps
                break
    if sum(ja)>sum(jo):
        print(count)
    else:
        print(-1) # partially correct
# the following code is fully correct        
t = int(input())
for i in range(t):
    n,m = map(int, input().split())
    ja = list(map(int, input().split()))
    jo = list(map(int, input().split()))
    ja.sort()
    jo.sort(reverse=True)
    count = 0
    x = 0
    for j in range(min(n, m)):
        if sum(ja) > sum(jo):
            break
        ja[x], jo[x] = jo[x], ja[x]
        x += 1
        count += 1

    if sum(ja) > sum(jo):
        print(count)
    else:
        print(-1)