# basics.py

x =  input("Input a command: ")
print("You entered {}.".format(x))
if x == 'a' or x == 'add': #remember to use the colon after the if, elif and else statements
    print("add")
    a = 1
    b = 2
    print("a = {}". format(a))
    c = a + b
    print("{} + {} = {}".format(a, b, c))
elif x == 's':
    print("subtract")
    a = 1
    b = 2
    c = a - b
    print("{}".format(c))
else:
    print("{} is not an active command".format(x))

print("Done")
