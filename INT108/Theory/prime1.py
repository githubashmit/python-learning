n=int(input("Enter number  "))
i=2
c=0
while i<n:
    if n%i==0:
        c=c+1
    i=i+1
if n<=1:
    print("Not prime number")
elif c==0 :
    print("prime number")
else:
    print("Not a prime")