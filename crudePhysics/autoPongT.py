import math
import time
import os
import random

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')


def placePlayers(box,players):
    for player in players:
        for i in range(player["top"],player["bottom"]+1):
            box[i][player["px"]] = '#'

def movePlayer(box, player,posY):
    #if ball is above the player
    if posY < player["top"]:
        box[player['bottom']][player["px"]] = ' '
        box[player['top']-1][player["px"]] = '#'
        player['top']-=1
        player['bottom']-=1

    #if ball is below the player
    if posY > player["bottom"]:
        box[player['bottom']+1][player["px"]] = '#'
        box[player['top']][player["px"]] = ' '
        player['top']+=1
        player['bottom']+=1





#This function builds the initial box  using the size given
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

#This parses the input to give the correct sizes
def parseInfo(string):
    string=string.split('x')
    return(string)

#Prints the box on the console
def printbox(box):
    for x in box:
        for i in x:
            print(i,end='')
        print('')




#I hate this functon very much and i don't want to look at it again!
def movement(box,x,y,orientation):
    if(box[y-1][x]=='#' and box[y][x+1]=='#' and box[y][x-1]=='#'):
        orientation='S'
    elif(box[y+1][x]=='#' and box[y][x+1]=='#' and box[y][x-1]=='#'):
        orientation='N'
    elif(box[y-1][x]=='#' and box[y+1][x]=='#' and box[y][x-1]=='#'):
        orientation='E'
    elif(box[y-1][x]=='#' and box[y+1][x]=='#' and box[y][x+1]=='#'):
        orientation='W'

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
    elif(orientation=='NE' and box[y][x+1]=='#' and box[y-1][x]=='#'):
        orientation = 'SW'
        box[y][x]=' '
        box[y+1][x-1]='O'
        x-=1
        y+=1
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
    elif(orientation=='SW' and box[y][x-1]=='#' and box[y+1][x]=='#'):
        orientation = 'NE'
        box[y][x]=' '
        box[y-1][x+1]='O'
        x+=1
        y-=1
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
    elif(orientation=='NW' and box[y][x-1]=='#' and box[y-1][x]=='#'):
        orientation = 'SE'
        box[y][x]=' '
        box[y+1][x+1]='O'
        x+=1
        y+=1
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
    elif(orientation=='SE' and box[y+1][x]=='#' and box[y][x+1]=='#'):
        orientation = 'NW'
        box[y][x]=' '
        box[y-1][x-1]='O'
        x-=1
        y-=1
    elif(orientation=='SE' and ((box[y+1][x+1]=='#') and (box[y][x+1]!='#'))):
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
    string = parseInfo(input("What is the box size? recommended:(70x20) -"))
    fps= 30
    posX = math.ceil(int(string[0])/2)
    posY =  math.ceil(int(string[1])/2)
    box= boxMaker(int(string[0]),int(string[1]))
    orientation='NW'
    ps = 0
    player1 = {
    "top":posY-2,
    "bottom":posY+2,
    "px": 3
    }
    player2 = {
    "top":posY-2,
    "bottom":posY+2,
    "px": int(string[0])-4
        }

    player = [player1,player2]
    placePlayers(box,player)
    printbox(box)
    while True:
        info=movement(box,posX,posY,orientation)
        if posX > int(string[0])-4 or posX<5:
            if ps==0:
                ps=1
            else:
                ps=0

        posY = info[1]
        posX = info[0]
        orientation= info[2]
        clearScreen()
        movePlayer(box,player[ps],posY)
        printbox(box)
        time.sleep(1/fps)


crudePhysics()
