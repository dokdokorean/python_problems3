import math
a,b=map(int,input().split())
print(int(math.factorial(a)/(math.factorial(a-b)*math.factorial(b))))
