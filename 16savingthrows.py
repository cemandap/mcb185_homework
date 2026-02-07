import random

DC  = 5 
iterations = 10000
adv = 0     # if adv = 0, none; if adv = 1, advantage; if adv = 2, disadvantage
def saving_throws(DC, adv): 
    survive_counter = 0
    total           = 0 
    for i in range(iterations):
        total += 1
        if adv == 1: 
            roll_1 = random.randint(1, 20)
            roll_2 = random.randint(1, 20)
            if roll_1 >= roll_2: roll = roll_1 
            else: roll = roll_2 
        elif adv == 2: 
            roll_1 = random.randint(1, 20)
            roll_2 = random.randint(1, 20)
            if roll_1 <= roll_2: roll = roll_1 
            else: roll = roll_2            
        else: roll = random.randint(1, 20) 
        if roll >= DC: survive_counter += 1 
    return survive_counter/total
       

print(saving_throws(5, 2))

