def gc_comp(dna):
    dna = dna.upper()
    gc = 0
    for nt in dna:
        if nt == 'G' or nt == 'C':
            gc += 1
    return gc / len(dna)

dna = input()
print(gc_comp(dna))

