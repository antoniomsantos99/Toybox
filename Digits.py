#Function that counts and prints the number of times a digit occurs in a number.
try: input = raw_input
except NameError: pass

number=input("What's your number? ")

for i in range(0,10):
    print(str(i) + ": " + str(number.count(str(i))))
t =input("Press any key to close")
