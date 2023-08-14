a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
d=max(a,b,c)
if a==d:
    if b+c>d:
        print('yes')
    elif b+c<=d:
        print('no')
elif b==d:
    if a+c>d:
        print('yes')
    elif a+c<=d:
        print('no')
elif c==d:
    if b+a>d:
        print('yes')
    elif b+a<=d:
        print('no')
