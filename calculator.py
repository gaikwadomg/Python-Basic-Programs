# requirement number1 num 2 and operator 
def calculate(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    elif operator =="%":
        return num1 % num2
    else:
        print("Unknown Operator")
    
num1 = input("Enter first number :")
num1 = float(num1)

operator = input("Enter operator + - * / %    :")
num2 = input("Enter number second :")
num2 = float(num2)

result = calculate(num1, operator, num2)
print(result)