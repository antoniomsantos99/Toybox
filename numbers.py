import os
import random

def SetScore(nome, score):
    file = open("scores.txt","a")
    file.write(nome + "-" + str(score) + "\n" )
    file.close()


def RepresentsInt(s):
    try:
        int(s)
        return False
    except ValueError:
        return True

nome = raw_input("What's your name? ")

level = 1
vida = 10
score = 0

while vida > 0:

 vida = 10
 number = random.randint(0,int(level)*15)

 #print "%i" % (number)

 while True:
   print "Level: %i (0-%i) // Lives : %i // Score : %i" % (level, level*15, vida, score)

   while True:
    escolha = raw_input("Choose a number: ")
    if RepresentsInt(escolha):
      print "That wont work %s!" % (nome)
    else:
      break

   os.system('cls' if os.name == 'nt' else 'clear')


   if int(escolha) == int(number):
     print("Nice one! Next level! \n")
     score += (level * 100) + (vida * level * 10)
     level += 1
     break
   else:

     vida -= 1

     if vida == 0 :
       print("You lost %s! Your score was: %i") % (nome, score)
       SetScore(nome, score)
       a = raw_input(" ")
       sys.exit()

     if int(escolha) < int(number):
       print("The number you chose is too SMALL!")
     else:
       print("The number you chose is too BIG!")

print "You lost!"
