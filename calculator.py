import arithmetic

def is_int(tokenList):
    for x in tokenList:
        try:
             int(x)
        except ValueError:
             return False
    return True

while True: 
    input = raw_input("> ")
    tokens = input.split() 
    if tokens[0] in ["q", "Q", "quit", "QUIT", "Quit"]:
        break
    if is_int(tokens[1:]):
        for x in range(1, len(tokens)):
            tokens[x] = int(tokens[x])

        operator = tokens[0]
        numbArgs = len(tokens) - 1
        allArgs = tokens[1:]

        if operator in ["+","add"] and numbArgs >= 2:
            print arithmetic.add(allArgs)
        elif operator in ["power", "pow"] and numbArgs >= 2:
            print arithmetic.power(allArgs)
        elif operator == "square" and numbArgs == 1:
            print arithmetic.square(allArgs)
        elif operator == "cube" and numbArgs == 1:
            print arithmetic.cube(allArgs)
        elif operator in ["*", "multiply"] and numbArgs >= 2:
            print arithmetic.multiply(allArgs)
        elif operator in ["-","subtract"] and numbArgs >= 2:
            print arithmetic.subtract(allArgs)
        elif operator in ["/", "divide"] and numbArgs >= 2:
            print arithmetic.divide(allArgs)
        elif operator in ["mod","%"] and numbArgs == 2:
            print arithmetic.mod(tokens[1], tokens[2])
        else:
            print "Incorrect number of inputs or incorrect operator."
    else:
        print "Arguments must be integers."

