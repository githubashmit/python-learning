n=int(input("Enter number of term u want to print of series = "))
a=0
b=1
print(a)
print(b)
n=n-2
while n>0:
    c=a+b
    d=b
    b=c
    a=d
    n=n-1
    print(c)

