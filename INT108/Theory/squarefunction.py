def square(n):
    for i in range(1,n+1):
        for j in range(1,n+10):
            if i==1 or j==1 or i==n:
                print("*",end="")