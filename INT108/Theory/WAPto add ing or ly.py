#WAP to add 'ing' or 'ly'
#input = xyz
#output = xyzing
#input = string
#output = stringly
str1=input()
s=str1[-3:-1]
s1=str1[-1]
s=s+s1
if s=="ing":
    print(str1+'ly')
else:
    print(str1+'ing')