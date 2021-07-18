t = int(input())
for x in range(t):
    n,k,e,m  = map(int,input().split())
    score = []
    for x in range(n-1):
        score.append(sum(list(map(int,input().split()))))
    my = sum(list(map(int,input().split())))
    score.sort(reverse = True)
    count = 0
    fin=score[k-1]-my+1
    if fin>m:
        print('Impossible')
    elif fin<0:
        print(0)
    else:
        print(fin)     