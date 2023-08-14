a=input()
for i in range(0,len(a)):
    if (a[i]=='+'):
        b=int(a[:i])
        c=int(a[i+1:])
        result=b+c
        print(b+c)
    elif (a[i]=='-'):
        b=int(a[:i])
        c=int(a[i+1:])
        result=b-c
        print(b-c)
    elif (a[i]=='*'):
        b=int(a[:i])
        c=int(a[i+1:])
        result=b*c
        print(b*c)
    elif (a[i]=='/'):
        b=float(a[:i])
        c=float(a[i+1:])
        d=b/c
        print('%.2f'%d)
        
