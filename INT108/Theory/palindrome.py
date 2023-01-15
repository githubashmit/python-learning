#simply i am reversing the string using for loop and then checking with the user string
n=input("Enter String to check whether it is palindrome or not ")
a=""
for i in n:
    a=i+a
print("reverse string is = ",a)
if a==n:
    print("palindrome")
else:
    print("Not palindrome")
