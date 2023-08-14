import math
a=input()
a=int(a)
x=0
for i in range(1,a+1):
    if math.sqrt(a-i)%1==0:
        x=i
        b=int(math.sqrt(a-x))
        break
print(x,b)
        

