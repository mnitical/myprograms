a=[]
for i in range(10):
    a.append(i)
for i in range(15):
    if i>9:
        i=i%9-1
    else:
        i=i
    print(a[i],end=' ')
    if i in [4,9]:
        print('\n')