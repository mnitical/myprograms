a={}
for x in list('hyyfyjdhgjhghkgkjgkyttrreewqwdassdxdxgfhgyujgku'):
    a[x]=a.get(x,0)+1
print(sorted(list(a.items()),key=lambda x:x[1],reverse=True))