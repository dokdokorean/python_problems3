a,b=map(int,input().split())
for j in range(a,b+1):
    for i in range(1,10):
        print(str(j)+'*'+str(i)+'='+str(int(j)*int(i)))
