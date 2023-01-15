#this code is to check prime .it divide the given number by 2 ,3,4 and so on till 50 depend on user choice gretaer than 50 or less than 50
#if the number get divide by any number one time i used break .so in this code bigger number can also be executed
#bigger prime number==813538384339
n=int(input("Enter number to check whether it is prime or not= "))
i=2
c=0
while i<n:
    if n%i==0 and i<=50:
        c=c+1
        if c==1:
            break
    elif i==50:
        break
    i=i+1
if n<=1:
    print("Not prime")
elif c==0 or n==2:
    print("Prime")
else:
    print("Not prime")
