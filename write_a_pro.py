# return more than one variable using one function
def fact(i):
    fact=1
    while i>0:
        fact*=i
        i-=1
    return fact,i,fact*0
x,y,z=fact(i=19)
print(x,y,z)
