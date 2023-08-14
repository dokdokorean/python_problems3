import math
a,b,c=map(int,input().split())
d=math.gcd(a,b)
e=int(a*(b/d))
f=math.gcd(e,c)
g=e*(c/f)
print(int(g))
