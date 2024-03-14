number1 = int(input("Enter first number: "))
number2 = int(input("Enter second numebr: "))
operation = input("Enter an operation: ")

if operation == '+':
    print(number1 + number2)
elif operation == '-':
    print(number1 - number2)
elif operation == '*':
    print(number1 * number2)
elif operation == '/':
    print(number1 / number2)
else:
    print("I didn't recognise that operation!")