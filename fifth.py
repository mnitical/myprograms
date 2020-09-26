a=[]
for i in 'Narendra':
    a.append(i)
for i in range(100):
    if i>7:
        i=i%7-1
        print(a[i],end=' ')
    else:
        i=i
        print(a[i],end=' ')
