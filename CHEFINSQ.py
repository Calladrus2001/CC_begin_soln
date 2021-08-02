from math import factorial as fact
for x in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    num = a[k-1]
    t = a.count(a[k-1])
    r = a[:k].count(num)
    print(fact(t)//(fact(r)*fact(t-r)))