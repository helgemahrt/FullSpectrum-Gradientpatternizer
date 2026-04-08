gradientstart = int(input('enter first color value (int):'))
gradientend = int(input('enter second color value (int):'))
size = int(input('enter size (layers) of gradient:'))

def generatepattern(a: int, b: int, ratioa: float, length: int) -> str:
    result = []
    error = 0.0

    for _ in range(length):
        error += ratioa
        if error >= 1.0:
            result.append(str(a))
            error -= 1.0
        else:
            result.append(str(b))

    return "".join(result)
    
def generategradient(a: int, b: int, size: int) -> str:
    ratios = [0.96,0.95,0.91,0.9,0.87,0.85,0.83,0.8,0.79,0.75,0.7,0.66,0.65,0.62,0.6,0.58,0.54,0.5,0.46,0.42,0.4,0.38,0.35,0.34,0.3,0.25,0.21,0.2,0.17,0.15,0.13,0.1,0.09,0.05,0.04]
    patterns = []
    patternsize = size // len(ratios)
    
    for ratio in ratios:
        patterns.append(generatepattern(a, b, ratio, patternsize))
    
    return "".join(patterns)
    
print(generategradient(gradientstart,gradientend,size))

input()
