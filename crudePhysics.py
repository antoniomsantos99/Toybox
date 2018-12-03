import math
import time
import os

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def boxMaker(w,h):
    l=[]
    line=[]
    box=[]

    for i in range(h):
      if i==0 or i == h-1:
        l.append('#'*w)
      else:
        l.append('#'+' '*(w-2)+'#')

    for i in l:
      for x in i:
        line.append((x))
      box.append(line)
      line=[]
    box[math.ceil(h/2)][math.ceil(w/2)]='O'
    return box

def parseInfo(string):
    string=string.split('x')
    return(string)

def printbox(box):
    for x in box:
        for i in x:
            print(i,end='')
        print('')

def initbox(box,w,h):
    box[math.ceil(h/2)][math.ceil(w/2)]='O'
    return [math.ceil(h/2),math.ceil(w/2)]


def movement(box,x,y,orientation):
    if(orientation=='N' and box[y-1][x]!='#'):
        box[y][x]=' '
        box[y-1][x]='O'
        y-=1
    elif(orientation=='N'):
        orientation = 'S'
        box[y][x]=' '
        box[y+1][x]='O'
        y+=1
    elif(orientation=='S' and box[y+1][x]!='#'):
        box[y][x]=' '
        box[y+1][x]='O'
        y+=1
    elif(orientation=='S'):
        orientation = 'N'
        box[y][x]=' '
        box[y-1][x]='O'
        y-=1

#East/West
    elif(orientation=='E' and box[y][x+1]!='#'):
        box[y][x]=' '
        box[y][x+1]='O'
        x+=1
    elif(orientation=='E'):
        orientation = 'W'
        box[y][x]=' '
        box[y][x-1]='O'
        x-=1
    elif(orientation=='W' and box[y][x-1]!='#'):
        box[y][x]=' '
        box[y][x-1]='O'
        x-=1
    elif(orientation=='W'):
        orientation = 'E'
        box[y][x]=' '
        box[y][x+1]='O'
        x+=1
#Corner Cases

#NE/SW

    if(orientation=='NE' and box[y-1][x+1]!='#'):
        box[y][x]=' '
        box[y][x+1]=' '
        box[y-1][x+1]='O'
        x+=1
        y-=1
    elif(orientation=='NE' and box[y][x+1]=='#'):
        orientation = 'NW'
        box[y][x]=' '
        box[y-1][x-1]='O'
        x-=1
        y-=1
    elif(orientation=='NE'):
        orientation = 'SE'
        box[y][x]=' '
        box[y][x+1]=' '
        box[y+1][x+1]='O'
        x+=1
        y+=1

    elif(orientation=='SW' and box[y+1][x-1]!='#'):
        box[y][x]=' '
        box[y][x+1]=' '
        box[y+1][x-1]='O'
        x-=1
        y+=1
    elif(orientation=='SW' and box[y][x-1]=='#'):
        orientation = 'SE'
        box[y][x]=' '
        box[y][x+1]=' '
        box[y+1][x+1]='O'
        x+=1
        y+=1
    elif orientation=='SW' and box[y+1][x]=='#':
        orientation = 'NW'
        box[y][x]=' '
        box[y][x+1]=' '
        box[y-1][x-1]='O'
        x-=1
        y-=1

    #NW/SE
    elif(orientation=='NW' and box[y-1][x-1]!='#'):
        box[y][x]=' '
        box[y][x+1]=' '
        box[y-1][x-1]='O'
        x-=1
        y-=1
    elif(orientation=='NW' and box[y][x-1]=='#'):
        orientation = 'NE'
        box[y][x]=' '
        box[y][x+1]=' '
        box[y-1][x+1]='O'
        x+=1
        y-=1
    elif(orientation=='NW'):
        orientation = 'SW'
        box[y][x]=' '
        box[y][x+1]=' '
        box[y+1][x-1]='O'
        x-=1
        y+=1
    elif(orientation=='SE' and box[y+1][x+1]!='#'):
        box[y][x]=' '
        box[y+1][x+1]='O'
        x+=1
        y+=1
    elif(orientation=='SE' and box[y+1][x]=='#'):
        orientation = 'NE'
        box[y][x]=' '
        box[y-1][x+1]='O'
        x+=1
        y-=1
    elif(orientation=='SE' and box[y][x+1]=='#'):
        orientation = 'SW'
        box[y][x]=' '
        box[y+1][x-1]='O'
        x-=1
        y+=1
    return [x,y,orientation]

def crudePhysics():
    string = parseInfo(input('What is the box size? ex:(15x20)'))
    posX = math.ceil(int(string[0])/2)
    posY =  math.ceil(int(string[1])/2)
    box= boxMaker(int(string[0]),int(string[1]))
    orientation='SE'
    printbox(box)

    while True:
        info=movement(box,posX,posY,orientation)

        posY = info[1]
        posX = info[0]
        orientation= info[2]
        clearScreen()
        printbox(box)
        time.sleep(0.05)


crudePhysics()
