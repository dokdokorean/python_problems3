a,b=input().split()
a=int(a)
b=int(b)
if b-30<0:
    c=a-1
    d=60+(b-30)
    if c<0:
        print((24+c),d)
    else:
        print(c,d)
else:
    print(a,(b-30))

    
