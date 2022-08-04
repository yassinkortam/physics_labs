
import pandas as pd
import random as rd

#constants
NUM_DICE = 500
TOT_TIME = 30

#integers
removed_die = 0
remaining_die = NUM_DICE

#arrays
removed_dice = [0]
remaining_dice = [NUM_DICE]

#Simulation
for i in range(TOT_TIME):
    for j in range(remaining_die):
        die_state = rd.randint(1,8)
        if die_state == 1:
            removed_die += 1
    remaining_die = NUM_DICE - removed_die   
    removed_dice.append(removed_die)
    remaining_dice.append(remaining_die)

#data output
d = {'Remaining Dice':remaining_dice, 'Removed Dice':removed_dice}
lab_data = pd.DataFrame(data=d)
print(lab_data)
lab_data.to_csv('half_life.csv')


    