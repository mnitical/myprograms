n=eval(input('enter height of Pascal triangle: '))
from math import factorial
def permutation(n):
    r=0
    a=[]
    while r<n+1:
        permut=factorial(n)//(factorial(n-r)*factorial(r))
        a.append(str(permut))
        r+=1
    return a
for i in range(n):
    a=permutation(i)
    print(('   '.join(a)).center(7*n+1))

