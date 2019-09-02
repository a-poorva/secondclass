# first_module.py

def addition(x,y):
    print("add")
    print("x = {}". format(x))
    z = x + y
    print("{} + {} = {}".format(x, y, z))
    return

def subtraction():
    print("subtract")
    c = a - b
    print("{}".format(c))
    return

def addsubtract(x, y, symbol):
    if symbol == "+":
        c = x+y
    elif symbol == "-":
        c = x-y
    else:
        c = "Unrecognized"
        return c

if __name__ == "__main__": #tells python to start running code from here

    x =  input("Input a command: ")
    print("You entered {}.".format(x))
    a = input("a= ")
    b = input("b= ")
    if x == 'a' or x == 'add': #remember to use the colon after the if, elif and else statements
        symbol = "+"
        answer = addsubtract(int(a),int(b), "+") #calling the previously defined function with paramaters
    elif x == 's':
        symbol = "-"
        answer = addsubtract(int(a),int(b), "-")
    else:
        print("Enter a new command")
        print("{} is not an active command".format(x))
    print("c = {}".format(answer))
    print("Done")
