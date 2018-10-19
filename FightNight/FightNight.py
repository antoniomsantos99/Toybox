import os
import random
import string
import json
import time


names_first = json.loads(open('Fighters-First.json').read())
names_last = json.loads(open('Fighters-Last.json').read())

money = 1000



def isNOTInt(s):
    try:
        int(s)
        return False
    except ValueError:
        return True

def betAction(money):
 fighterPointer = raw_input("Who do you wanna bet?")

 while True:

    betBank = raw_input("How much do you want to bet?")
    if int(betBank) > money or isNOTInt(betBank):
        print "Invalid input or not enough money"
    else:
        money = money - int(betBank)
        print("%i %i") % (money, int(betBank))
        return money

def fight(odd1):
    randnum = random.randint(0,100)
    print randnum
    if(randnum < odd1):
        print("%s wins") % (fname1)
        winner = 1
    else:
        print("%s wins") % (fname2)
        winner = 2




#for name in names_first:
while True:

    if(money == 0):
        print("You are broke! The End.")
        time.sleep(5)
        break

    str1 = random.randint(0,100)
    def1 = random.randint(0,100)
    int1 = random.randint(0,100)
    agi1 = random.randint(0,100)
    stm1 = random.randint(0,100)
    lck1 = random.randint(0,100)
    #hp1 = 3 * def1 + 9 * stm1
    power1 = float((str1 + def1 + int1 + agi1 + stm1 + lck1) / 6)
    #power1 = 5 * str1 + 2 * int1 + 2 * agi1 + 1.5 * lck1
    fname1 = (random.choice(names_first) + " " +  random.choice(names_last))

    str2 = random.randint(0,100)
    def2 = random.randint(0,100)
    int2 = random.randint(0,100)
    agi2 = random.randint(0,100)
    stm2 = random.randint(0,100)
    lck2 = random.randint(0,100)
    power2 = float((str2 + def2 + int2 + agi2 + stm2 + lck2) / 6)
    #hp2 = 3 * def2 + 9 * stm2
    #power2 = 5 * str2 + 2 * int2 + 2 * agi2 + 1.5 * lck2
    fname2 = (random.choice(names_first) + " " +  random.choice(names_last))

    total = power1+power2
    odd1 = ((power1/total)) * 100
    mult1 = (1/(power1/total))
    odd2 = 100 - odd1
    mult2 = (1/(power2/total))
    print("\n         %s        VS      %s\n\nSTR %i || DEF %i || INT %i           STR %i || DEF %i || INT %i \nAGL %i || STM %i || LCK %i           AGL %i || STM %i || LCK %i\n") % (fname1, fname2, str1, def1, int1, str2, def2, int2, agi1, stm1, lck1, agi2, stm2, lck2)
    print("    Power: %i                     Power: %i   ") % (power1 ,power2)
    print("    Odd: %i (%fX)                       Odd: %i (%fX)  ") % (odd1,mult1 ,odd2, mult2)
    print("\n Money: %i") % (money)


    #betAction(money)
    fighterPointer = raw_input("Who do you wanna bet?")

    while True:
        betBank = raw_input("How much do you want to bet?")
        if int(betBank) > money or isNOTInt(betBank):
            print "Invalid input or not enough money"
        else:
            money = money - int(betBank)
            print("%i %i") % (money, int(betBank))
            break


    #fight(odd1)

    randnum = random.randint(0,100)
    print randnum
    if(randnum < odd1):
        print("%s wins") % (fname1)
        winner = 1
    else:
        print("%s wins") % (fname2)
        winner = 2

    if int(fighterPointer) == int(winner):
        print("You win")
        if(winner == 1):
            money += (int(betBank) * mult1)
        else:
            money += (int(betBank) * mult2)
    else:
        print("You lose")
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
