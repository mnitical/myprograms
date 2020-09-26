import math
count=0
for i in range(1,101):
    square=math.pow(i,2)
    a=str(square)
    if a[-3]=='1':
        count+=1
print(count)