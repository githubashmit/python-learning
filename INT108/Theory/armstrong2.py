#armstrong number 153   1^3+5^3+3^3=153
#1634= 1^4+6^4+3^4+4^4=1634
n=int(input("Enter number = "))
s=n
b=len(str(n))
sum=0
while n!=0:
    r=n%10
    sum=sum+(r**b)
    n=n//10
if s==sum:
    print("Armstrong")
else:
    print("not Armstrong")