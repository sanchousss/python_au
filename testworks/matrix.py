n=int(input('n = '))

lst = [[0 for i in range(n)] for j in range(n)]
line = n
s = 1
round = 0
side = 1
o0,o1,o2=0,1,2

while line !=0:
    if side==1:
        side=2
        for i in range(o0, n-o1+1):
            lst[o0][i]=s
            s+=1
    elif side==2:
        side=3
        for i in range(o1, n-o1+1):
            lst[i][n-o1]=s
            s+=1
    elif side==3:
        side=4
        for i in range(n-o2, o0-1, -1):
            lst[n-o1][i]=s
            s+=1
    else:
        side=1
        for i in range(n-o2, o1-1, -1):
            lst[i][o0]=s
            s+=1
        o0,o1,o2=o0+1,o1+1,o2+1
    round+=1
    if round % 2 !=0:
        line-=1

for i in range(n):
    print(lst[i])