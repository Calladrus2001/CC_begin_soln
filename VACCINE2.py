t = int(input('enter no of test cases: '))
for x in range(t):
    tot,perday = map(int,input().split())
    age = list(map(int,input().split()))
    count_risk = 0
    count = 0
    curr_day = 1
    for x in age:
        if x >= 80 or x <= 9:
            count_risk += 1
        else:
            count += 1
    if count_risk%perday==0:
        curr_day = curr_day + (count_risk//perday)
    else:
        curr_day = curr_day + (count_risk//perday) + 1
    if count%perday==0:
        curr_day += count//perday
    else:
        curr_day += count//perday +1      
    print(curr_day)   #wrong       