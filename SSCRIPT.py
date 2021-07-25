t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    count = 0
    max = 0
    for x in s:
        if x == '*':
            count += 1
            if count > max:
                max = count
        else:
            count = 0
    if max >= k:
        print('Yes')
    else:
        print('No')
