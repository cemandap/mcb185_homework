import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

sames = 0

for _ in range(trials):
    classroom = []
    same_birthday = False

    for _ in range(people):
        birthday = random.randint(0, days - 1)
        if birthday in classroom:
            same_birthday = True
            break
        classroom.append(birthday)

    if same_birthday:
        sames += 1

print(sames / trials)
