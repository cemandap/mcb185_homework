# python3 gc_analysis AAGACCCAAAAAAAAGATTA 7
import sys
seq = sys.argv[1]
k = int(sys.argv[2])
for i in range(len(seq) - k +1):
	win = seq[i:i+k]
	g = win.count('G')
	c = win.count('C')
	gc_comp = (c+g)/k
	gc_skew = (g-c)/(g+c) if g+c != 0 else 0
	if g+c == 0: gc_skew = 0
	else: 		  gc_skew = (g-c) / (g+c)
	print(i, win, c, g, gc_comp, gc_skew)