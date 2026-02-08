import random 

def deathsaves(): 
    iterations = 100
    total = 0 
    died = 0 
    stabilized = 0 
    revived = 0 

    for i in range(iterations): 
        failure = 0 
        stable = 0 

        while True: 
            roll = random.randint(1, 20)

            if roll == 20: 
                revived += 1 
                total += 1 
                break 

            elif roll == 1: 
                failure += 2             

            elif roll < 10:    
                failure += 1 

            else:  
                stable += 1 

            if stable >= 3: 
                stabilized += 1 
                total += 1 
                break 

            if failure >= 3: 
                died += 1
                total += 1 
                break 

    return f"Died:{100 * died/total}%, Stabilized:{100 * stabilized/total}%, Revived:{100 * revived/total}%"

print(deathsaves())

