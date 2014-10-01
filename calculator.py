import arithmetic

def valid_operator(tokenList):
    operators = ["+", "-", "/", "*", "square", "cube", "pow", "mod"]
    print "Token list length: ",len(tokenList)
    
    if tokenList[0] in operators and len(tokenList) >= 3:
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
        # make a loop to int all the tokens
        tokens[1] = int(tokens[1])
        tokens[2] = int(tokens[2])
        if tokens[0] == "+":
            print arithmetic.add(tokens[1],tokens[2])
