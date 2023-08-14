a,b=input().split()
a=int(a)
b=int(b)
if a==1:
    a=a+399
elif a==2:
    a=a+338
elif a==3:
    a=a+167
elif a==4:
    a=a+96
elif a==5:
    a=a+65
if b==1:
    b=b+399
elif b==2:
    b=b+338
elif b==3:
    b=b+167
elif b==4:
    b=b+96
elif b==5:
    b=b+65
if (a+b)>500:
    print('angry')
else:
    print('no angry')
