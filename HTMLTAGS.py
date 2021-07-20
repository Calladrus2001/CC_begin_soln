import re
t = int(input())
for x in range(t):
    s = input()
    if re.match('^</.*>', s):
        print('Success')
    else:
        print('Error')
