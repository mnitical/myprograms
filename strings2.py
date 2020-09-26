a='abcde'
b='ABCDE'
c=''
i=0
if len(a)==len(b):
    for j in b:
        c+=j
        c+=a[i]
        i+=1
else:
    exit('a and b have different lengths')
print(c)
