from string import *
a=[word for i in open('how to focus.txt') for word in (i.strip()).split()]
b=[]
for i in a:
    n=a.index(i)
    for x in i:
        if x not in ascii_letters:
            i=i.replace(x,'')
            a[n]=i
    if i!='':
        b.append(i)
print(b)

'''a=[line.strip() for line in open('how to focus.txt')]
b=open('how to focus2.txt','w')
for i in a:
    if i.startswith('1.'):
        print(i,file=b)'''
'''f=open('writeafile.txt',"w")
print('I am starting writing a new file.\nPlease review it.',file=f)
f.close()

.read()
 '''

