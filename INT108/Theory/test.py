#input= python is a programming language
#output =Python Is A Programming Language
def string_k(str1):
    text =str1.split()
    s=""
    for i in text:
        string=i.capitalize()
        s=s+" "+string
    print(s[1:])
str1=input()
string_k(str1)
