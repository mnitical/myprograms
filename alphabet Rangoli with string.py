n=eval(input('enter size of Rangoli: '))
import string as st
a=st.ascii_lowercase
a=a[:n]
b=a
c=[]
a=a[::-1]
x=(2 * (n - 1))*2+1
for i in range(n):
    print(('-'.join(a[0:i+1]+b[n-i:n:1])).center(x,'-'))
    c.append(i)
c.pop()
c.reverse()
for i in c:
    print(('-'.join(a[0:i + 1] + b[n - i:n:1])).center(x,'-'))