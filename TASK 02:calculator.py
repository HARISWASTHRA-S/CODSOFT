def calculator():
    print("Welcome to the Simple Calculator!")
    while True:
        print("\nSelect an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
              
        operation = input("Enter the number of the operation (1/2/3/4): ")
        
        if operation not in ['1', '2', '3', '4']:
            print("Invalid operation choice. Please try again.")
            continue

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue
        
        # Perform calculation
        if operation == '1':
            result = num1 + num2
            print(f"The result of {num1} + {num2} is {result}")
        elif operation == '2':
            result = num1 - num2
            print(f"The result of {num1} - {num2} is {result}")
        elif operation == '3':
            result = num1 * num2
            print(f"The result of {num1} * {num2} is {result}")
        elif operation == '4':
            if num2 == 0:
                print("Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"The result of {num1} / {num2} is {result}")

        
        choice = input("\nDo you want to perform another calculation? (yes/no): ").strip().lower()
        if choice not in ['yes', 'y']:
            print("Thank you for using the calculator! Goodbye!")
            break

calculator()
