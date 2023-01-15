def min_of_three(x,y,z):
    c=0
    if x<=y:
        c=x
    else:
        c=y
    if c<=z:
        c=c
    else:
        c=z
    return c
x=int(input("Enter number= "))
y=int(input("Enter number= "))
z=int(input("Enter number= "))
print("Minimum number is = ",min_of_three(x,y,z))