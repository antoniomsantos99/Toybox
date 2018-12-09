import random
import os
import time

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def printList(list,tries):
    for i in list:
        print(str(i).zfill(len(str(max(list)))) +'-| <' + i * '=' + '>')
    print('Shuffled ' + str(tries) + ' times!')


def is_sorted(data):
    for i in range(len(data) - 1):
        if data[i] > data[i + 1]:
         return False
    return True

def bogosort(data):
 tries = 0
 printList(data,tries)
 while not is_sorted(data):
    clearScreen()
    random.shuffle(data)
    tries+=1
    printList(data,tries)
 return data

def bubblesort(list):
    tries = 0
    for iter_num in range(len(list)-1,0,-1):
        for idx in range(iter_num):
            clearScreen()
            if list[idx]>list[idx+1]:
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp
            tries+=1
            printList(list, tries)

def insertion_sort(InputList):
    tries = 0
    for i in range(1, len(InputList)+1):
        clearScreen()
        printList(InputList,tries)
        j = i-1
        try:
            nxt_element = InputList[i]
        except:
            return 1
        while (InputList[j] > nxt_element) and (j >= 0):
            InputList[j+1] = InputList[j]
            j=j-1
            tries+=1
        InputList[j+1] = nxt_element



mode = input("bubblesort(0)|insertion_sort(1)|monkeysort(2)")
size =int(input("What's the size of your list?"))
start = time.time()
if mode == '0':
    bubblesort(random.sample(range(size), size))
if mode == '1':
    insertion_sort(random.sample(range(size), size))
if mode == '2':
    bogosort(random.sample(range(size), size))
print('Done in ' + str(round(time.time()-start,4)) + ' seconds!!')
stilldontknowhowtoanykey= input('')
