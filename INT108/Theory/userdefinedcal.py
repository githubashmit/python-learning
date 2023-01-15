#user defined function
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
while True:
    #Printing message for better clarity to the user
    print("select the operation that you want to perform")
    print("1.Addition")
    print("2.substract")
    print("3.multiply")
    print("4.division")
    print("5.terminate")
    choice=input("choose 1/2/3/4/5 ")#Taking input from the user to perform specific task
    if choice in ('1','2','3','4'):
        n1=float(input("Enter the first number "))
        n2=float(input("Enter the second number "))
    if choice =='1':
        print(add(n1,n2))
    elif choice=='2':
        print(sub(n1,n2))
    elif choice=='3':
        print(mul(n1,n2))
    elif choice=='4':
        print(div(n1,n2))
    elif choice=='5':
        break
    else:
        print("wrong option")
