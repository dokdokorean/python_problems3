a=input()
a=int(a)
if a%4==0 and a%100!=0:
    print('yes')
elif a%400==0:
    print('yes')
else:
    print('no')
