seq = 'ACTAAACTAGT'

for i, nt in enumerate(seq):
	if nt == 'A':
		run_start = i
		run_length = 1
		for j in range(i+1, len(seq)):
			if seq[j] == 'A': run_length += 1
			else: break
		print(run_start, run_length)