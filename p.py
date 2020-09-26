def fact(x):
    i=1
    i*=x
    x-=1
    if x==0:
        return i
    fact(x)


print(fact(2))