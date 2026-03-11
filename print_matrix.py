import sys

alph = sys.argv[1]
mat = sys.argv[2]
mis = sys.argv[3]

#for spacing in between letters and after
print('  ', end='')
for nt in alph:
	print(nt,end=' ')
print()

for nt in alph:
	print(nt, end=' ')
	for nt2 in alph:
		if nt == nt2:
			print(mat, end=' ')
		else:
			print(mis, end=' ')
	print( )
