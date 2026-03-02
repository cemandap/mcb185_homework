import sys

# collect numbers from command line
vals = []
for s in sys.argv[1:]:
    vals.append(float(s))

# sort in preparation for median (and min, max)
vals.sort()

# mean
total = 0
for val in vals:
    total += val
mean = total / len(vals)

# median
mid = len(vals) // 2
if len(vals) % 2 == 1:
    median = vals[mid]
else:
    median = (vals[mid] + vals[mid - 1]) / 2

print("minimum:", vals[0])
print("maximum:", vals[-1])
print("range:", vals[-1] - vals[0])
print("average:", mean)
print("median:", median)