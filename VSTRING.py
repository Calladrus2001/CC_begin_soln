t = int(input())
for x in range(t):
    #n,c = map(int,input().split())
    s = input()
    st = []
    for x in s :
        st.append(x)
    s1 = st
    s1 = s1[-1:] + s1[:-1]
    print(st)
    print(s1)