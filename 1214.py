a,b=input().split()
a=int(a)
b=int(b)
if a%4==0 and a%100!=0:
    if b==2:
        print('29')
elif a%400==0:
    if b==2:
        print('29')
else:
    if b==1 or b==3 or b==5 or b==7 or b==8 or b==10 or b==12:
        print('31')
    if  b==4 or b==6 or b==9 or b==11:
        print('30')
    if b==2:
        print('28')

