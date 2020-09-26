for i in range(10,100):
    x=i
    y=int(str(i)[::-1])
    z=x+y
    z1=int(str(z)[::-1])
    sum=1
    while z1!=z:
        z=z1+z
        z1=int(str(z)[::-1])
        sum+=1
    if sum>20:
        print(x,y,z,z1)