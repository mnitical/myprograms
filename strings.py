a='narendrasainipulelablockbandikui'
b=a.lower()
c=''
n=0
for i in b:
    if i==b[2*n+1]:
        c+=i.upper()
        n+=1
    else:
        c+=i
print(c)