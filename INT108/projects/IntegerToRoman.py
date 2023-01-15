def integerConversion(num):
    if num == 0:
        return ""

    if num <= 3:
        if num == 1:
            return "I"
        num = num - 1
        return integerConversion(num) + "I"
    elif num == 4:
        return "IV"
    elif num <= 8:
        if num == 5:
            return "V"
        num = num - 1
        return integerConversion(num) + "I"
    elif num == 9:
        return "IX"

    elif num <= 30:
        if num == 10:
            return "X"
        num = num - 10
        return integerConversion(num) + "X"
    elif num == 40:
        return "XL"
    elif num <= 80:
        if num == 50:
            return "L"
        num = num - 10
        return integerConversion(num) + "X"
    elif num == 90:
        return "XC"

    elif num <= 300:
        if num == 100:
            return "C"
        num = num - 100
        return integerConversion(num) + "C"
    elif num == 400:
        return "CD"
    elif num <= 800:
        if num == 500:
            return "D"
        num = num - 100
        return integerConversion(num) + "C"
    elif num == 900:
        return "CM"

    elif num == 1000:
        return "M"
    num = num - 1000
    return integerConversion(num) + "M"


def numberOfDigit(num):
    if num <= 9:
        return 1
    return numberOfDigit(num / 10) + 1


def intToRoman(num):
    roman = ""
    length = numberOfDigit(num)
    for i in range(0, length):
        roman = integerConversion(int(num % 10) * pow(10, i)) + roman
        num = int(num / 10)

    return roman


print(intToRoman(int(input("Enter number which you want to convert into roman= "))))