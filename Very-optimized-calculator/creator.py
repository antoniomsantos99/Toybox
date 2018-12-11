f = open("calculator.py", "w")
signals = ['+','-','x',':']
size = input("How many numbers can the calculator handle? (ex: 50 -> maximum calculation is (50x50))")
try:
    size=int(size)+1
except:
    print('Invalid Value')
    SystemExit()

f.write("a=int(input('What is the first number?'))\nb=int(input('What is the second number?'))\nsignal=input('What is the signal?(+,-,x,:)')\n")


for signal in signals:
    if signal == ':': start=1
    else: start=0
    for a in range(size):
        for b in range(start,size):
            first = "if a == " + str(a) + " and b == " + str(b) + " and signal == " + '"' + signal + '": \n'
            if signal == '+':
                second =' print("The sum of ' + str(a) + " and " + str(b) + ' is ' + str(a+b) + '")'
            if signal == '-':
                second =' print("The subtraction of ' + str(a) + " and " + str(b) + ' is ' + str(a-b)+'")'
            if signal == 'x':
                second =' print("The product of ' + str(a) + " and " + str(b) + ' is ' + str(a*b) +'")'
            if signal == ':':
                second =' print("The division of ' + str(a) + " and " + str(b) + ' is ' + str(round((a/b),4)) +'")'
            second = second+'\n'
            f.write(first)
            f.write(second)
f.write('idontknowhowtopresstocontinue=input("")')
