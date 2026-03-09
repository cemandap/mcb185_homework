import sys

if len(sys.argv) <2:
	print("python triples.py")
	sys.exit()

n = int(sys.argv[1])

for a in range(1, n+1):
	for b in range(a+1, n+1):
		c = (a**2 + b**2)**0.5
		if c % 1 == 0 and c <= n:
			print(a, b, int(c))