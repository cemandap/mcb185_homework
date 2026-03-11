#!/usr/bin/env python3
import sys
import mcb185

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    name = defline.split()[0]
    length = len(seq)

    print(name, end=' ')
    for nt in 'ACGTN':
        print(seq.count(nt) / length, end=' ')
    print()