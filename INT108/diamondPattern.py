#diamond pattern
n=int(input())
i=1
k=1
n1=1
j=n-1
n2=n-1
i1=1
while i<=n:
  while j>0:
    print(" ",end="")
    j=j-1
  n1=k
  while n1>0:
    print("*",end="")
    n1=n1-1
  k=k+2
  i=i+1
  n2=n2-1
  j=n2
  print()
k=k-4
a1=n-1
while a1>0:
  k1=k
  i2=1
  while i2<=i1:
    print(" ",end="")
    i2=i2+1
  while k1>0:
    print("*",end="")
    k1=k1-1
  k=k-2
  k1=k
  i1=i1+1
  a1=a1-1
  print()