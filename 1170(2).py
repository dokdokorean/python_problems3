a,b,c=input().split()
b=int(b)
c=int(c)
if c<10:
    c='00'+str(c)
elif c<100:
    c='0'+str(c)
if b<10:
    b='0'+str(b)
print(a+str(b)+str(c))
