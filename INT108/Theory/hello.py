def fun(int1, str1):
  for i in range(0,10):
    print(int1*2)
    return str1
int1 = int(input())
str1 = input()
print(fun(int1,str1))