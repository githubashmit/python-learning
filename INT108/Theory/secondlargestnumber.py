numlist=[]
number=int(input("Enter the length of the list = "))
for i in range(1,number+1):
    value=int(input("please enter the number which u want in list = "))
    numlist.append(value)
print("Your list is= ",numlist)
for i in range(number-1):
    for j in range(i+1 , number):
        if (numlist[i]>numlist[j]):
            temp = numlist[i]
            numlist[i]=numlist[j]
            numlist[j]=temp
print("your sorted list is= ",numlist)
print("Seconnd largest number is= ",numlist[1])
