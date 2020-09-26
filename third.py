x=eval(input('enter no of elements in Fibo series: '))
a=[1,1]
total_int_sq_root_elements_in_series=0
for i in range(1,x-1):
    a.append(a[i]+a[i-1])
for i in range(x):
    b=a[i]**(1/2)
    if b.is_integer():
        total_int_sq_root_elements_in_series+=1
    else:
        continue
print(total_int_sq_root_elements_in_series)