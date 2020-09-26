b=[]
sum=0
import random
for i in range(6):
    a=[]
    while len(a)!=6:
        x=random.randint(0,1)
        if x==1:
            sum+=1
        if sum>12:
            a.append(0)
        else:
            a.append(x)
    b.append(a)
print(b)