def cal(x):
    if x%2==0:
        return "even"
    else:
        return "odd"
print("Enter number to check whether its is even or not ")
n=int(input())
print(cal(n))