#Use the for loop to determine how many times the digit is in the number

def Analyze(number,digit,total):
 count = 0
 for d in number:
     if d == digit:
         count +=1
 print str(digit) + " : " + str(count)


total = 0
digit = 0

number = raw_input("What number you want? ")

while digit < 10:
    Analyze(number,str(digit),total)
    digit += 1
t = raw_input("Press any key to close")
