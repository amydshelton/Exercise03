import arithmetic

def valid_operator(tokenList):
    operators = ["+", "-", "/", "*", "square", "cube", "power", "mod"]
  #  print "Token list length: ",len(tokenList)
    
    if tokenList[0] in operators:
        my_bool = True
        #print "my_bool: %r" % my_bool
        for x in range(1, len(tokenList)):
            #print " x = %r" % x
            #print " tokenList = %r" % tokenList[x]
            if tokenList[x].isdigit() == False:
                print "I don't understand."
                my_bool = False
        return my_bool
    else:
        print "I don't understand."
        return False

while True: 
    input = raw_input("> ")
    tokens = input.split() 
    if tokens[0] == "q" or tokens[0] == "Q":
        break
    if valid_operator(tokens):
        for x in range(1, len(tokens)):
            tokens[x] = int(tokens[x])
        if tokens[0] == "+" and len(tokens) >= 3:
            print arithmetic.add(tokens[1:])
        elif tokens[0] == "power" and len(tokens) == 3:
            print arithmetic.power(tokens[1], tokens[2])
        elif tokens[0] == "square" and len(tokens) == 2:
            print arithmetic.square(tokens[1])
        elif tokens[0] == "cube" and len(tokens) == 2:
            print arithmetic.cube(tokens[1])
        else:
            print "I don't understand."