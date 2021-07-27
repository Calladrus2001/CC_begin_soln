for t in range(int(input())):
    n = int(input())
    max = 0
    boys = list(map(int, input().split()))
    boys.sort(reverse=True)
    girls = list(map(int, input().split()))
    girls.sort()
    for i in range(n):
        y = boys[i]+girls[i]
        if max < y:
            max = y
    print(max)
