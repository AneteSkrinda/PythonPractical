while True:
    num1 = float(input("Enter first number: ")) # Takes user input
    num2 = float(input("Enter second number: "))
    operation = input("Enter an operation (*, /, +, -, %): ")
    
    if operation not in ['*', '/', '+', '-', '%']: # Checks if operation is valid
        print("Operation provided isn't valid, please, try again.")
        continue
    
    if operation == '*':  # Performs operation and prints result
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2
    elif operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '%':
        result = num1 % num2
    
    print("Result:", result)
    
    choice = input("Do you want to perform another calculation? (y/n): ") # Asks user if they want to continue
    if choice.lower() != 'y':
        break