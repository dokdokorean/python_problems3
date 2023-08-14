import io, sys
a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
if (a-b+c)%10==0:
    print('대박')
else:
    print('그럭저럭')
