f=open('perepis.txt','r')
c=0
x=int(input())
y=int(input())
for i in f:
    L=i.split()
    b=L[3][-4:]
    a=int(b)
    if(a<1978):
        print(L[0])
        c+=1
    if x<a<y:
        print(L)
print(c)
