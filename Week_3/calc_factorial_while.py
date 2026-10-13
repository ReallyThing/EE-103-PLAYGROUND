number = int(input("Enter a number to calculate its factorial: "))

if number < 0:
    print("Factorial is not defined for negative numbers. Please enter a non-negative integer.")
    number = int(input("Enter a number to calculate its factorial: "))

else:
    factorial = 1
    i = 1
    while i <= number:
        factorial *= i
        i += 1
    print(f"The factorial of {number} is: {factorial}")