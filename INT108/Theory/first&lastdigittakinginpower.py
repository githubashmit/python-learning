#12345   ==5^1 and checking even and odd
n=int(input("Enter number = "))
a=n%10
sum=0
while n>0:
    b=n%10
    sum=sum*10+b
    n=n//10
b=sum%10
c=a**b
print(c)
if c%2==0:
    print("Even")
else:
    print("odd")