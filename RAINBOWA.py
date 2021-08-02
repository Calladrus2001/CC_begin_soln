t=int(input())
for i in range(t):
    N=int(input())
    array=list(map(int,input().split()))
    a={1,2,3,4,5,6,7}
    if array==[i for i in array[::-1]] and set(array)==a:
        print("yes")
    else:
        print("no")
