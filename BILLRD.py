import sys
t = int(input())
for x in range(t):
    n,k,x,y = map(int,input().split())
    if x == y:
        print (n,n)
    count = 0
    if x > y:
        while count<k:
            if count < k:
                while x < n:
                    x+=1
                    y+=1
                coll = [x,y]
                count+=1
            else:
                for x in coll:
                    print(x,end = ' ')
                sys.exit(0)        
            while y < n:
                y += 1
                x -= 1
            if count < k :
                coll = [x,y]
                count+=1
            else:
                for x in coll:
                    print(x,end = ' ')
                sys.exit(0)
            while x > 0:
                x -=1
                y -=1
            if count<k:
                coll = [x,y]    
                count+=1
            else:
                for x in coll:
                    print(x,end = ' ')
                sys.exit(0)
            while y > 0:
                x +=1
                y-=1
            if count<k:
                coll = [x,y]
                count+=1  
            else:
                for x in coll:
                    print(x,end = ' ')
                sys.exit(0)           
    elif y > x:
        while count < k:
            if count < k:
                while y < n:
                    x+=1
                    y+=1
                coll = [x,y]
                count += 1
            else:
                for x in coll:
                    print(x,end = ' ')
                sys.exit(0)
            while x < n:
                x+=1
                y-=1
            if count < k:
                coll = [x,y]
                count+=1
            else:
                for x in coll:
                    print(x,end = ' ')
                sys.exit(0)
            while y > 0:
                x-=1
                y-=1
            if count < k:
                coll = [x,y]
                count += 1
            else:
                for x in coll:
                    print(x,end = ' ')
                sys.exit(0)
            while x > 0:
                x-=1
                y+=1
            if count < k:
                for x in coll:
                    print(x,end = ' ')
                sys.exit(0)                              # correct but TLE                      