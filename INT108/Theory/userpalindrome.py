def reverse(num):
    num1=0
    num2=num
    while num >0:
        a=num%10
        num1=num1*10+a
        num=num//10
    if num1==num2:
        return "Palindrome"
    else:
        return "Not palindrome"
num=int(input("Enter number = "))
print(reverse(num))