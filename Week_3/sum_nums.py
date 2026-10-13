number = input("Enter a number to calculate its sum from 1 to this number: ")
sum = 0
if number <= 0:
    print("Please enter a positive integer.")
else:
 i = 1
while i <= int(number):
    sum += i
    i += 1
print(f"The sum of numbers from 1 to {number} is: {sum}")

sum_gauss = int(number) * (int(number) + 1) // 2

if sum == sum_gauss:
    print("My running sum code works correctly.")
else:
    print("My running sum code failed badly.")