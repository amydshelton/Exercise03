import arithmetic

def valid_operator(tokenList):
    operators = ["+", "-", "/", "*", "square", "cube", "power", "mod", "add", 
    "divide", "subtract", "multiply", "%", "pow"]
  #  print "Token list length: ",len(tokenList)
    
    if tokenList[0] in operators:
        my_bool = True
        for x in range(1, len(tokenList)):
            if tokenList[x].isdigit() == False:
                print "I don't understand."
                my_bool = False
                break
        return my_bool
    else:
        print "I don't understand."
        return False

while True: 
    input = raw_input("> ")
    tokens = input.split() 
    if tokens[0] in ["q", "Q", "quit", "QUIT", "Quit"]:
        break
    if valid_operator(tokens):
        for x in range(1, len(tokens)):
            tokens[x] = int(tokens[x])
        if tokens[0] in ["+","add"] and len(tokens) >= 3:
            print arithmetic.add(tokens[1:])
        elif tokens[0] in ["power", "pow"] and len(tokens) >= 3:
            print arithmetic.power(tokens[1:])
        elif tokens[0] == "square" and len(tokens) == 2:
            print arithmetic.square(tokens[1])
        elif tokens[0] == "cube" and len(tokens) == 2:
            print arithmetic.cube(tokens[1])
        elif tokens[0] in ["*", "multiply"] and len(tokens) >= 3:
            print arithmetic.multiply(tokens[1:])
        elif tokens[0] in ["-","subtract"] and len(tokens) >= 3:
            print arithmetic.subtract(tokens[1:])
        elif tokens[0] in ["/", "divide"] and len(tokens) >= 3:
            print arithmetic.divide(tokens[1:])
        elif tokens[0] in ["mod","%"] and len(tokens) == 3:
            print arithmetic.mod(tokens[1], tokens[2])
        else:
            print "I don't understand."