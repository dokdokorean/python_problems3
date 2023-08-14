a=int(input())
b=0
c=0
for i in range(1,a):
    if i%a==0:
        c=b+1
    else:
        c=b+0
if c==1:
    print('composite')
elif c==0:
    print('prime')
    
    
