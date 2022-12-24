# f=open("ummy.txt","x")
# f.close()                           here to create file ummy and dummy...as i am appended so i commented here
f=open("ummy.txt","a")
f.write("hello me ashmit")
f=open("ummy.txt","r")
print(f.read())