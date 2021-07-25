# method 1
# runs but shows nzec while submitting
t = int(input())
for x in range(t):
    c = int(input())
    d = [0, 2, 4, 8, 16, 32, 64, 128, 256]
    end = 0
    for y in d:
        if y > c:
            end = y
            break
    arr = []
    arr1 = []
    for a in range(end//2):
        for b in range(end//2, end):
            if a ^ b == c:
                arr1.append(a)
                arr1.append(b)
                arr.append(arr1)
                arr1 = []
    product = []
    for z in arr:
        a = z[0]*z[1]
        product.append(a)
    print(max(product))

# method 2
# AC
for i in range(int(input())):
    n = int(input())
    x = bin(n)[2:]
    a, b = "", ""
    for i in range(len(x)):
        if x[i] == '0':
            a += '1'
            b += '1'
        elif i == 0 and x[i] == '1':
            a += '1'
            b += '0'
        elif i != 0 and x[i] == '1':
            a += '0'
            b += '1'

    print(int(a, 2)*int(b, 2))
