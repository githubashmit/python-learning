try:
    f=open("dummy.txt")    #have or not have what file
    try:
        f=open("dummy.txt","w")
        f.write("Hello class")
        f = open("dummy.txt", "r")
        print(f.read())
    except:
        print("Error during writing")
    finally:
        f.close()
except:
    print("Error in opening file")