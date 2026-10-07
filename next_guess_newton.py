x = float(input("What x to find the square root of?"))
g = float(input("What guess to start with?"))
if x < 0:
    print("Cannot find the square root of a negative number.")  
elif x == 0:
    print("The square root of 0 is 0.")
else:
    
    while True:
        next_g = (g + x / g) / 2
        if abs(next_g - g) < 1e-10:
            g = next_g
            break
        g = next_g

    print("Approximate square root:", g)