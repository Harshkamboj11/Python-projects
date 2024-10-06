a = int(input("enter first number: "))
b = int(input("enter second number: "))

operator = input("enter the operator(+,-,*,%,/): ")

sum = a+b
subtract = a-b
multiply = a*b
divide = a/b
modulus = a%b

if operator == '+':
    print(f"The sum of the numbers is {sum}")
elif operator == '-':
    print(f"The difference of the number is {subtract}")
elif operator == '*':
    print(f"The multiplication of the number is {multiply}")
elif operator == '/':
    print(f"the divison of the number is {divide}")
elif operator == '%':
    print(f"the modulus of the number is {modulus()}")
else:
    print("invalid operation.....")