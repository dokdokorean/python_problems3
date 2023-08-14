import io, sys
a,b=input().split()
a=int(a)
b=int(b)
if a%2==0:
    print('짝수+',end='')
elif a%2!=0:
    print('홀수+',end='')
if b%2==0:
    print('짝수=',end='')
elif b%2!=0:
    print('홀수=',end='')
if (a+b)%2==0:
    print('짝수')
else:
    print('홀수')

