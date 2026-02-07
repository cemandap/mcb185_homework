import math

for i in range(1, 100):
	a = i
	for n in range (1, 100):
	    b = n
	    hypo = math.sqrt(a ** 2 + b ** 2)
	    if hypo % 1 == 0: print(a, b, hypo)
