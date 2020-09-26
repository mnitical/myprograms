a='01689'
for i in range(1,10000):
    if set(str(i)).issubset(set(a)):
        b=list(str(i))
        x=0
        while x<len(b):
            if b[x]=='6':
                b[x]='9'
                x+=1
            if x>len(b)-1:
                break
            if b[x]=='9':
                b[x]='6'
            x+=1
        b=''.join(b)
        if b==str(i)[::-1]:
            print(b)
