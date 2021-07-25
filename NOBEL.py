t = int(input())
for x in range(t):
    a = {}
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    for y in arr:
        a[y] = a.get(y,0) + 1
    if len(a)<m:
        print('Yes')
    else:
        print('No')    