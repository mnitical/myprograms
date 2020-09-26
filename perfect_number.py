for i in range(1,10000):
    sum=0
    for x in range(1,i):
        if i%x==0:
            sum+=x
        else:
            continue
    if sum==i:
        print(i)