t = int(input())
for x in range(t):
    s = input()
    l = []
    count = 0
    for i in range(len(s)):
        if s[i] == '1':
            n = l.count('1')
            if n == 0:
                try:
                    if s[i+1]!='1':
                        count+=1
                except:
                    if i == len(s)-1:
                        count+=1
            else:
                l.append(s[i])
        if s[i] == '0':
            n = l.count('1')
            if n > 1:
                count +=1
                l = []
    print(count)