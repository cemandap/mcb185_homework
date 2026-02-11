import math

for a in range(1, 20):
	
	
	for b in range(1, 20):
		c = math.sqrt(a**2 + b**2)
		if math.isclose(c % 1, 0):
			print(a, b, c)