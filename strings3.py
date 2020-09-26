a='abcdefghijklmnopqrstuvwxyz'
for i in range(26):
    for j in range(26):
        k=j+i
        if k > 25:
            k = (k-1) % 25
        print(a[k],end='')
    print()
