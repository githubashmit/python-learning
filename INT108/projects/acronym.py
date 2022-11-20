n=int(input())
li=[]
li1=[]
f=""
for i in range(1,n+1):
    str=input()
    li.append(str)
for i in li:
    c=i
    e=len(i)
    d=c[0].upper()
    f=f+d
    d=d+c[1:e]
    li1.append(d)
print(f)
print(li1)
