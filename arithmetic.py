#take as many as is given, min 2

def add(numList):
    return sum(numList)

def subtract(numList):
    total = numList[0] - sum(numList[1:])
    return total

def multiply(numList):
    total = 1
    for i in numList:
        total = total * i
    return total

def divide(numList):
    if 0 in numList[1:]:
        return "You can't divide by zero, dummy!!" 
    elif numList[0] == 0:
        total = 0.
        return total
    else:
        total = numList[0]*numList[0]
        for i in numList:
            total = float(total) / float(i)
        return total

def power(numList):
    total = numList[0]
    x = 1
    while x < len(numList):
        total = total**numList[x]
        x += 1
    return total


#take exactly 1

def square(num1):
    return pow(num1, 2)

def cube(num1):
    return pow(num1, 3)


#take exactly 2

def mod(num1, num2):
    return num1 % num2


