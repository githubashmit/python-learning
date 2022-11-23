def find_char(str1 , char):
    c=0
    for i in str1:
        c=c+1
        if i==char:
            return c
str1=str(input("Enter word = "))
char=str(input("Enter letter which u want to search in word= "))
if find_char(str1,char)==None:
    print("Not found")
else:
    print(find_char(str1,char))