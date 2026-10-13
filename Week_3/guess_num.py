import random

loop_number = 1
number = random.randint(0,10)
guess = int(input("Guess my number."+" "))
while True:
    if guess == number:
     victory_message = f"You win. The number was {number}."
     print(victory_message)
     break
    else:
     print("not it. Again."+" ")
     guess = int(input())
     loop_number = loop_number+1
     if loop_number == 5:
        
         while True:
             print("Oh, nooooooo!") #Is it supposed to loop infinitely? It will fill the terminal...
         break
             
         