n = int(input())
bud = []
for x in range(n):
    bud.append(int(input()))
bud.sort(reverse=True)
max = -100
for x in range(n):
    start = bud[x]*(x+1)
    if start > max:
        max = start
print(max)