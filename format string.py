for i in range(8):
    print(f"{'-'.join('NARENDRA'[0:i+1]):^18s}"*5)
for i in range(7,0,-1):
    print(f"{'-'.join('NARENDRA'[0:i]):^18s}"*5)
'''
'{:},{:} '.format(a,b)
< left justified
> right justified
^ center justified
d---for integer
f---for float
s---for strings
between </>/^   x.y  d/f/s
            x=total length
            y=after decimal
            in strings y represent length of string
'''
