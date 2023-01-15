f1=open("Mine2.jpg","rb")
# print(f1.read())
f2=open("abc.jpg","wb")
for x in f1:
    f2.write(x)