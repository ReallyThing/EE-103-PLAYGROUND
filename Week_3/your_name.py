name = str(input("Input your name."+" "))

E = f"Aho54yu{name}42z.89tur"

extracted_name = E[7:-9]
print(f"My name is {extracted_name}!")
answer = str(input("Do you want me to reverse your name?(Y/N)"))

if answer == "Y" or answer == "y":
     print ("Your reversed name is:" + " " + extracted_name[::-1])
elif answer == "N" or answer == "n":
     print("Okay. Have a nice day.")
else:
     print("Please enter Yes(Y) or No(N).")