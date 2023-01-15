str1=input()
def consonants(str1):
    str2=""
    for i in str1:
        if i=="a" or i=="e"or i=="i"or i=="o"or i=="u":
            continue
        str2=str2+i
    return str2
if consonants(str1)=="":
    print("Empty")
else:
    print(consonants(str1))