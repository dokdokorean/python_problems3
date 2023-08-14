import math
a,b,c=map(int,input().split())
d=math.gcd(a,b)
e=math.gcd(d,c)
print(e)
