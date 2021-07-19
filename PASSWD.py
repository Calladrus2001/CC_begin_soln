import re
t = int(input())
for x in range(t):
    s = input()
    if re.match(".{10,}",s):
        if re.match(".*[a-z]+.*",s):
            if re.match("^[^[A-Z]].*[A-Z]+.*[^[A-Z]]$",s):
                if re.match("^[^[0-9]].*[0-9]+.*[^[0-9]]$",s):
                    if re.match("^[^['@','#','%','&','?']].*['@','#','%','&','?']+.*[^['@','#','%','&','?']]$",s):
                       print('YES')
                    else:
                        print('NO') 
                else:
                    print('NO')
            else:
                print('NO')
        else:
            print('NO')  
    else:
        print('NO') 