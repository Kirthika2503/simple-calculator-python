 # A simple calculator

operator = input("Enter an operator(+,-,*,/,**,%):  ")
num1 =int(input("Enter the first number:  "))
num2 =int(input("Enter the second number:  "))

result = None # initialize the variable so that when result is
               # asked to print no runtime error occurs

if operator == "+":
    result = num1 + num2

elif operator == "-":
    result = num1 - num2

elif operator == "*":
    result = num1 * num2

elif operator == "/": # clashes with % when num2 is 0
    if num2 !=0:
        result = num1 / num2
    else:
        print("Error: Division by zero")

elif operator == "**":
    result = num1 ** num2

elif operator == "%": # clashes with / when num2 is 0
    if num2 !=0:
        result = num1 % num2
    else:
        print("Error: Modulo by zero")

else:
    print(f"{operator} is not valid")

if result is not None:
    print(f"The result is {round(result,2)}")
