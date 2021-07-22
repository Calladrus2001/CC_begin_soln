t = int(input())
for x in range(t):
    n = int(input())
    op = 0
    trip = 0
    comm = list(map(str,input().split()))
    for x in comm:
        if x == 'start':
            op = 1
        if x == 'restart':
            if op == 1:
                op = 1
            elif op == 0:
                op = 1    
        if x == 'stop':
            if op == 0:
                trip = 1
            elif op == 1:
                op = 0
    if trip == 1:
        print("404")
    else :
        print("200")                    