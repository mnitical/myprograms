import random
# The prize is behind=1
right_door,i,j=0,0,0
winbyself_decn=0
winbymonty_offer=0
# a is switch status
a=[True, False]
while i<10000:
    right_door=random.randint(1,3)
    u_chose=random.randint(1,3)
    if u_chose==right_door and random.choice(a):
        winbyself_decn+=1
    elif (u_chose!=right_door) and random.choice(a):
        winbymonty_offer+=1
    i += 1
print(winbyself_decn,winbymonty_offer,i,j)
print(f'winning % by not switching={(winbyself_decn/10000)*100} and winning % by switching={(winbymonty_offer/10000)*100}')