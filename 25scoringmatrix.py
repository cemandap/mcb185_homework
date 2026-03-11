import sys

alph = sys.argv[1]
mat = sys.argv[2]
mis = sys.argv[3]

print('  ', end=' ')
for nt in alph:
    print(nt, end='   ')
print()

for nt1 in alph:
    print(nt1, end=' ')
    for nt2 in alph:
        if nt1 == nt2:
            print(mat, end=' ')
        else:
            print(mis, end=' ')
    print()
