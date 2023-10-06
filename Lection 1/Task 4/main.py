"""Calculator"""

# pylint: disable=C0103

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
operation = input ("Enter the operation: ")
result = None

match operation:
    case "+":
        result = number1 + number2
    case "-":
        result = number1 - number2
    case "*":
        result = number1 * number2
    case "/":
        if number2==0:
            print("division by zero")
        else:
            result = number1 / number2
    case "^":
        result = number1 ** number2
    case "root":
        result = number1 ** (1 / number2)

if result is not None:
    print(result)
