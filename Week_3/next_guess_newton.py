x = float(input("What x to find the cube root of? "))
g = float(input("What guess to start with? "))

print("Current estimate cubed:", g ** 3)

if g == 0:
	if x == 0:
		next_g = 0.0
		print("Next guess:", next_g)
	else:
		print("Next guess cannot be calculated from a zero estimate.")
else:
	next_g = (2 * g + x / (g * g)) / 3
	print("Next guess:", next_g)
