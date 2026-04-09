import json
from os import system

datajunkie = False
match input('Do you want some Data for insights about the Gradient?(bool): '):
    case "1" | "true" | "True" | "y" | "yes":
        datajunkie=True
system("clear||cls")
def log(msg: str):
    if datajunkie:
        print(msg)  
        

def getratioarray(stepsize: int, lowerbound: int, upperbound: int) -> list:
    array = []
    step = upperbound/100
    while step >= lowerbound/100:
        array.append(round(step,2))
        step -= (stepsize/100)
    log("Count of ratios: "+str(len(array)))
    log("Ratios: "+json.dumps([i * 100 for i in array]))
    return array
    
def generatepattern(a: int, b: int, ratioa: float, length: int) -> str:
    result = []
    error = 1.0

    for _ in range(length):
        error += ratioa
        if error >= 1.0:
            result.append(str(a))
            error -= 1.0
        else:
            result.append(str(b))

    return "".join(result)
    
def generategradient(a: int, b: int, size: int, offset: int, ratiostepsize: int, lowerbound: int, upperbound: int) -> str:
    ratios = getratioarray(ratiostepsize, lowerbound, upperbound)
    patterns = []
    patternsize = size // len(ratios)
    log("Amount of layers per ratio: "+str(patternsize))
    for _ in range(offset):
        patterns.append(str(a))
    
    for ratio in ratios:
        patterns.append(generatepattern(a, b, ratio, patternsize))
    
    return "".join(patterns)

gradientstart = int(input('enter first color value (int): '))
gradientend = int(input('enter second color value (int): '))
size = int(input('enter size/layers of gradient (int): '))

lowerbound = input('enter lower mixing bound, defaults to 0% (int): ')
try:
    if int(lowerbound) > 0:
        lowerbound = int(lowerbound)
    else:
        lowerbound = 0
except:
    lowerbound = 0
    
upperbound = input('enter upper mixing bound, defaults to 100% (int): ')
try:
    if int(upperbound) < 100:
        upperbound = int(upperbound)
    else:
        upperbound = 100
except:
    upperbound = 100
    
gradientoffset = input('enter offset in layers from the bottom, defaults to 0 (int): ')
try:
    if int(gradientoffset) > 0:
        gradientoffset = int(gradientoffset)
    else:
        gradientoffset = 0
except:
    gradientoffset = 0
    
smallgradient = input('enter gadient stepsize, defaults to 5% (int): ')
try:
    if int(smallgradient) >= 0:
        smallgradient = int(smallgradient)
    else:
        smallgradient = 5
except:
    smallgradient = 5
      
print('')    
gradient = generategradient(gradientstart,gradientend,size,gradientoffset, smallgradient, lowerbound, upperbound)
print('')
print('Output:')
print(gradient)

input()
