import random
import sys


cal = int(sys.argv[1])
num = int(sys.argv[2])


shared_birthdays = 0
rounds = 50


for g in range(rounds):
    shared = False
    birthdays = []


    for _ in range(num):
        birthdays.append(random.randint(0, cal-1))


    for i in range(num):
        for j in range(i+1, num):
            if birthdays[i] == birthdays[j]:
                shared = True


    if shared:
        shared_birthdays += 1


print(shared_birthdays / rounds)
