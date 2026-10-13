number_for_factorial = int(input("Enter a number to calculate its factorial: "))

for i in range(1, number_for_factorial + 1):
    factorial = 1
    for j in range(1, i + 1):
        factorial *= j
    print(f"The factorial of {i} is: {factorial}")