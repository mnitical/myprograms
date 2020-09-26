import random
score=0
x=random.randint(1,10)
i=0
guess_num=[]
while i<5:
    y=random.randint(1,10)
    guess_num.append(y)
    if x!=y:
        score-=1
    elif x==y:
        score+=10
    i+=1
print(x,guess_num,score)