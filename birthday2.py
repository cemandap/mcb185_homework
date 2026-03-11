import sys
import random


cal = int(sys.argv[1])
num = int(sys.argv[2])


calendar = [0] * cal


for _ in range(num):
    date = random.randint(0, cal-1)
    calendar[date] += 1


shared = False
for date in range(cal):
    if calendar[date] > 1:
        shared = True


if shared:
    print('hooray')
else:
    print('not this time')
