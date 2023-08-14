a,b=map(int,input().split())
result=0
for i in range(a,b+1):
    if i%2==0:
        result-=i
        print('-'+str(i),end='')
    else:
        result+=i
        if a-i==0:
            print(a,end='')
        else:
            print('+'+str(i),end='')
if result>0:
    print('='+'+'+str(result))
else:
    print('='+str(result))


        
