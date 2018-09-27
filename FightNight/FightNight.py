import os
import random
import string
import json
import time


names_first = json.loads(open('Fighters-First.json').read())
names_last = json.loads(open('Fighters-Last.json').read())

for name in names_first:
    str = random.randint(0,100)
    defe = random.randint(0,100)
    int = random.randint(0,100)
    agi = random.randint(0,100)
    stm = random.randint(0,100)
    lck = random.randint(0,100)
    power = (str + defe + int + agi + stm + lck) / 6
    print(random.choice(names_first) + " " +  random.choice(names_last) + " \n  STR %i || DEF %i || INT %i \n  AGI %i || STM %i || LCK %i \n POWER: %i") % (str, defe, int, agi, stm, lck, power)
    time.sleep(2)
