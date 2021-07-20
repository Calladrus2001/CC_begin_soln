def reverse(a):
    rev = ""
    num = len(a)
    j = num - 1
    for i in range(0, num):
        rev += a[j]
        j -= 1
    return rev


pal = []
for x in range(10000):
    if str(x) == reverse(str(x)):
        pal.append(x)

t = int(input())
for x in range(t):
    i = int(input())
    for x in pal:
        if x > i:
            print(x)
            break

# runs perfectly in vs code but doesnt in CC compiler
