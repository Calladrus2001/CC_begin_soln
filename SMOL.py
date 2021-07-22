t = int(input())
for x in range(t):
    n,k = map(int,input().split())
    if k == 0:
        print(n)
    else:    
        a = n//k
        print(n-a*k)