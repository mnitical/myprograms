# if break execute in between loop, then else will not execute
'''num=11
for i in range(2,num):
    if num%i==0:
        print('Not Prime')
        break
else:
    print('Prime')'''

import random
a=random.randint(1,10)
for i in range(5):
    b = eval(input('enter guessed int (1-10): '))
    if b!=a:
        print('Not correct ...your rest chances for guessing',4-i )
    elif b==a:
        print('you won')
        break
else:
    print('you lose try again')