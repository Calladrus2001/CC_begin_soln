import sys
t = int(input())
for x in range(t):
    n,k = map(int,input().split())
    q = list(map(int,input().split()))
    curr_day = 0
    carry = 0
    for y in q:
        carry = carry - (k - y)
        curr_day = curr_day + 1
        if carry<0:
            print(curr_day)
            sys.exit(0)
        elif carry == 0:
            print(curr_day + 1)   
            sys.exit(0)
    while carry >= 0: 
        carry -= k
        curr_day +=1
    print(curr_day)
# the above code is wrong
# the following is correct
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    q = [int(i) for i in input().split()]
    day,status,q_remaining = 1,False, 0
    for i in q:
        q_total = i + q_remaining
        q_remaining = q_total - k
        if q_remaining < 0 :
            print(day)
            status = True
            break
        day+=1
    if status == False:
        print( day+( q_remaining//k))    