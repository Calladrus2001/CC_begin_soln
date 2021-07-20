d1,v1,d2,v2,p = map(int,input().split())
curr_day = 1
stock = 0
if min(d1,d2)==d1:
    vac1 = v1
    vac2 = v2
else:
    vac1 = v2
    vac2 = v1
for x in range(100):
    while curr_day < min(d1,d2):
        curr_day = curr_day + 1
    while curr_day < max(d1,d2) and stock < p:
        stock = stock + vac1
        curr_day = curr_day + 1
    while stock<p:      
        stock = vac1 + vac2 + stock
        curr_day = curr_day + 1
    print(curr_day-1)
    break              