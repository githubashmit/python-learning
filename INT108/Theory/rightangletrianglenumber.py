def rev_triangle(rows):
    for i in range(0,rows+1):
        for j in range(rows-i,0,-1):
            print(j,end=" ")
        print()
rows = int(input("Number of rows = "))
rev_triangle(rows)