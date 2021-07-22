t = int(input())
for x in range(t):
    n,k = map(int,input().split())
    s = list(map(int,input().split()))
    s.sort()
    print(s[k-1] - s[0]) 