import random

the_number = random.randint(0, 9)
guess = int(input("Guess a number between 0 and 9: "))
while True:
    if guess == the_number:
        print("You did it. It was " + str(the_number) + ".")
        break
    else:
        print("Nuh uh.")
        guess = int(input("Guess a number between 0 and 9: "))