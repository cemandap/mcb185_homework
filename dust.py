#dust, entropy filter
import math
def entropy(s):
	pa = s.count('A')/len(s)
	pc = s.count('C')/len(s)
	pg = s.count('G')/len(s)
	pt = s.count('T')/len(s)
	h = 0
	if pa != 0: h -= pa * math.log2(pa)
	if pc != 0: h -= pc * math.log2(pc)
	if pg != 0: h -= pg * math.log2(pg)
	if pt != 0: h -= pt * math.log2(pt)
	return h
	
seq = 'ACTGTAAAAAAACGTACGT'
k = 5
for i in range(len(seq)-k+1):
	win = seq[i:i+k]
	print(i, win, entropy(win))