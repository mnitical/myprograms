l=eval(input('enter height of A (only greater than 3): '))
print(' ' * (l - 1), '*',sep='')
for i in range(l-1,0,-1):
    if i==l//2:
        print(' ' * (i - 1), '*', '*' * (2 * (max(range(l - 1, 0, -1)) - i) + 1), '*', sep='')
    else:
        print(' '*(i-1),'*',' '*(2*(max(range(l-1,0,-1))-i)+1),'*',sep='')
print(3//2)