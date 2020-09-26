# using .join() we can join a list of strings in a single string
import random
a='three'
b=list(a)
random.shuffle(b)
a=''.join(b)
print(a)