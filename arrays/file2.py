f=open("lpu.txt","a")
f.write("   hi i am append    ")
f.write("    hello   ")
f.close()
f=open("lpu.txt","r")
print(f.read())
f=open("lpu.txt","w")
f.write("Hi i am ashmit")
f.close()
f=open("lpu.txt","r")
s=""
for i in f.read():
    s=i+s
print(s)
print(f.read())
f.close()
