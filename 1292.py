a=str(input())
b=0
for i in a:
    b+=int(i)
if b%7==4:
    print('suspect')
else:
    print('citizen')
    
