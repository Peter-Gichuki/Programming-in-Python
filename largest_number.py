#program to find the largest of three numbers
num1=int(input("Enter the first number="))
num2=int(input("Enter the second number="))
num3=int(input("Enter the third number="))
if num1>num2 and num1>num3:
    print(num1," is greater than ",num2, " and ",num3)
if num2>num1 and num2>num3:
    print(num2," is greater than",num1, " and ",num3)
if num3>num1 and num3>num2:
    print(num3," is greater than ",num1, " and ",num2)