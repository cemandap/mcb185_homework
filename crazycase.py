import sys

def crazycase(s):
	out = ''
	for i, ch in enumerate(s):
		out += ch.lower() if i % 2 == 0 else ch.upper()
	return out
	
print(crazycase(' '.join(sys.argv[1:])))	