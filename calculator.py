import arithmetic

def valid_operator(tokenList):
    if tokenList[0] in ["+", "-", "/", "*", "square", "cube", "pow", "mod", "q"] and tokenList[1].isdigit() and tokenList[2].isdigit():
        return True
    else:
        print "I don't understand."
        return False

#def valid_ints(token1, token2):
#    if token1.isdigit() and token2.isdigit():
#        return True
#    else:
#        print "I don't understand."
#        return False        

while True: 
    input = raw_input("> ")
    tokens = input.split()
    if valid_operator(tokens):

   # try:
   #     tokens[1] = int(tokens[1])
   #     tokens[2] = int(tokens[2])
   # except ValueError:
   #     print "I don't understand."

        if tokens[0] == "q" or tokens[0] == "Q":
            break
        if valid_operator(tokens):
            tokens[1] = int(tokens[1])
            tokens[2] = int(tokens[2])
            if tokens[0] == "+":
                print arithmetic.add(tokens[1],tokens[2])
