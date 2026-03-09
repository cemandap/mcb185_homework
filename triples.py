for a in range(1,15):
	for b in range(a+1, 15):
		c = (a**2 + b**2)**0.5
		if c % 1 != 0: continue
		print(a,b,c)