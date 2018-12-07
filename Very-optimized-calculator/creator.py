f = open("calculator.py", "w")
signals = ['+','-','x',':']
size = input("How many numbers can the calculator handle? (ex: 50 -> maximum calculation is (50x50))")
try:
    size=int(size)+1
except:
    print('Invalid Value')
    SystemExit()
f.write("from creator import parser \n \nlist=parser() \n \na=int(list[0])\nb=int(list[2])\nsignal =list[1]\n\n")


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

def parser():
    eq= input("What's your equation?")

    if '+' in eq:
      eq=eq.split('+')
      eq.insert(1,'+')
    if '-' in eq:
      eq=eq.split('-')
      eq.insert(1,'-')
    if 'x' in eq:
      eq=eq.split('x')
      eq.insert(1,'x')
    if ':' in eq:
      eq=eq.split(':')
      eq.insert(1,':')

    return eq
