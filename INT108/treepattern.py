#tree pattern
n=int(input())
i=1
k=1
n1=1
j=n-1
n2=n-1
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