import random
a=[]
i=1
while i<=100:
    a.append(random.randint(0,1))
    i+=1
print(a)
count=[]
sum=0
for i in a:
    if i==0:
        sum+=1
    elif i==1:
        count.append(sum)
        sum=0
print(count)
print(max(count))
#b=str(a).replace(',' ,'')
#print(b)