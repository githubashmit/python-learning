try:
    x=5/0
    print(x)
    # a=[1,2]
    # print(a[4])
    #print(a)
except NameError:
    print("a is not defined")
except:
    print("Something is not working")