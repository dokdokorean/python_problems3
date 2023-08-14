print('종료하려면 음수를 입력하시오')
a=0
c=0
while True:
    b=int(input('성적을 입력하시오: '))
    if b<0:
        print('성적의 평균은',a/c,'입니다.')
        break
    a+=b
    c+=1
    b=0

