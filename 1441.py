a=(input())
l=list()
for i in a:
    l.append(i)
l.sort(key=lambda x:x[0],reverse=True)
for i in l:
    for j in i:
        print(j,end=' ')
    print()
