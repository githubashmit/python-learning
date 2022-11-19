#In this code i am diving user's number with 1 ,2,and so on till n its long process
n=int(input("Enter number to check whether it is prime or not= "))
i=1
count=0
while i<=n:
        if n%i==0:
                count=count+1
        i=i+1
if count==2:
        print("Prime number")
else:
        print("Not a prime number")

