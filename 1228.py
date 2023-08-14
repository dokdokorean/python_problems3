a,b=input().split()
a=float(a)
b=float(b)
pm=(a-100)*0.9
bm=(b-pm)*100/pm
if bm<=10:
    print('정상')
elif bm<=20:
    print('과체중')
else:
    print('비만')
