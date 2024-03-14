while True:
    try:
        number1 = int(input("Enter your first number: "))
        number2 = int(input("Enter your second number: "))
    except ValueError:
        print("Please type a number!")
        continue
    break

while True:
    operation = input("Enter operation: ")

    match operation:
        case '+':
            print(number1 + number2)
            quit()
        case '-':
            print(number1 - number2)
            quit()
        case '*':
            print(number1 * number2)
            quit()
        case '/':
            print(number1 / number2)
            quit()