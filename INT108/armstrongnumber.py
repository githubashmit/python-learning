#armstrong number 153   1^3+5^3+3^3=153
#1634= 1^4+6^4+3^4+4^4=1634
a=int(input("Enter number= "))
n=a
i=0
c=0
n1=a
while n>0:
    n=n//10
    i=i+1

while a>0:
    b=a%10
    b=b**i
    c=c+b
    a=a//10
if c==n1:
    print("Armstrong number")
else:
    print("Not armstrong number")

