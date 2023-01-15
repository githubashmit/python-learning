a=9
b=8
c=sum((a,b))
print(c)      #built in function

def function1():
    print("Hello you are in function 1")
function1()
function1()
function1()
function1()
print(c)

def function2(a,b):
    print("Hello you are in function 1",a+b)
function2(3,4)

def function3(a,b):
    """This is a function which will calculate average of two numbers"""
    avg=(a+b)/2
    print(avg)
    return avg
function3(5,7)
v=function3(5,7)
print(v)
print(function3.__doc__)
