"""You are given a sequence A1,A2,…,AN. Find the maximum value of the expression 
|Ax−Ay|+|Ay−Az|+|Az−Ax| over all triples of pairwise distinct valid indices (x,y,z)."""
t = int(input())
n = int(input())
seq = list(map(int,input().split()))
largest = 0
for x in seq:
    for y in seq:
        for z in seq:
            exp1 = x - y
            if exp1 < 0 :
                exp1 = y - x
            exp2 = y - z
            if exp2 < 0:
                exp2 = z - y
            exp3 = z - x
            if exp3 < 0 :
                exp3 = x - z
            exp = exp1 + exp2 + exp3
            if exp > largest :
                largest = exp
print(largest)                