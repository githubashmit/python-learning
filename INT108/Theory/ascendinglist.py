#In this code i am creating list from user and arranging them in ascending order
li=[]
c=0
e=0
n=int(input("Enter how many elements you want in list= "))
for i in range(1,n+1):
    ele=int(input("Enter one number which u want in list= "))
    li.append(ele)
print("Your list is= ",li)
i=len(li)
while True:
    e=0
    d=len(li)
    while d-1>0:
        if li[e]>li[e+1]:
            c=li[e]
            li[e]=li[e+1]
            li[e+1]=c
        d=d-1
        e=e+1
    i=i-1
    if i==1:
        break
print("list in ascending order is = ",li)
