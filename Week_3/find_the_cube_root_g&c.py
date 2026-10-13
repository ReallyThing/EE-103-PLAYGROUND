import math 

number = int(input("Enter a number to find its cube root: "))

cube_root = number ** (1/3)
print("The cube root of", number, "is", cube_root)

if number < 0:
    cube_root = -(-number) ** (1/3)
    print("The cube root of", number, "is", cube_root)