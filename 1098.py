a,b=map(int,input().split())
c=int(input())
d=[[0]*a for i in range(b)]
for i in range(c):
    q,w,e,r=map(int,input().split())
    d[e-1][r-1]=1
    if w==0:
        for i in range(q):
            d[e-1][r+i-1]=1
    elif w==1:
        for i in range(q):
            d[e+i-1][r-1]=1

for i in d:
    for j in i:
        print(j,end=' ')
    print()
