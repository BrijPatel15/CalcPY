import re

print("My first Calculator")
print("Type quit to exit\n")

previous = 0; # holds the result of prev calculation
run = True

def performMath():
    global run #because run is a global var and not in the scope otherwise
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter Equation: ")
    else :
        equation = input(str(previous))
    if equation == 'quit':
        run = False
        print("Turning off")
    else :
        equation = re.sub('[a-zA-Z,.()" "]', '', equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)

        print(previous)

while run:
    performMath()
