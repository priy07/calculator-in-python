print("****** SIMPLE CALCULATOR ******")
print()

# Get the first value from the user
num1 = float(input("Enter the First Value = "))
print()

# Get the second value from the user
num2 = float(input("Enter the Second Value = "))

print()
print("Press + for Addition")
print("Press - for Subtraction")
print("Press * for Multiplication")
print("Press / for Division")

# Get the operation choice from the user
operation = input("Enter your choice of operation: ")
print()

# Perform the chosen operation
if operation == '+':
    result = num1 + num2
    print(f"The result of {num1} + {num2} is: \n {result}")
elif operation == '-':
    result = num1 - num2
    print(f"The result of {num1} - {num2} is: \n {result}")
elif operation == '*':
    result = num1 * num2
    print(f"The result of {num1} * {num2} is: \n {result}")
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"The result of {num1} / {num2} is: \n {result}")
    else:
        print("Error! Division by zero.")
else:
    print("Invalid operation!")
