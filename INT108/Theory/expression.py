#Python  as it is even number of letter so ans pyt
#hints as it has odd number of letter so ans hin
def first_half(str1):
    l=len(str1)
    if l%2==0:
        s=l
        return str1[:s//2]
    else:
        s=l+1
        return str1[:s//2]
str1=input()
print(first_half(str1))