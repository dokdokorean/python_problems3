a,b = input().split()
a= int(a)
b= int(b)
if(a % 10 == 0):
  c= b + int((90 - a) / 5)
else:
    c = b + int((90 - a) / 5) + 1
print(c)
