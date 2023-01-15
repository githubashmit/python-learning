#45673   4^3=64 return true and false according to even and odd
a=input()
c=len(a)
d=a[0]
e=a[c-1]
calc=pow(int(d),int(e))
print(calc)
print(calc % 2==0)