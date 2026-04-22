import json
from os import system

datajunkie = False
match input('Do you want some Data for insights about the Gradient?(bool): '):
    case "1" | "true" | "True" | "y" | "yes":
        datajunkie = True
system("clear||cls")

def log(msg: str):
    if datajunkie:
        print(msg)


def parse_color(color_str: str) -> dict:
    color_str = color_str.strip()
    if ':' not in color_str:
        return {int(color_str): 1.0}
    mix = {}
    for part in color_str.split(','):
        filament, pct = part.strip().split(':')
        mix[int(filament.strip())] = float(pct.strip()) / 100.0
    total = sum(mix.values())
    return {k: v / total for k, v in mix.items()}


def getratioarray(stepsize: int, lowerbound: int, upperbound: int) -> list:
    array = []
    step = upperbound / 100
    while step >= lowerbound / 100:
        array.append(round(step, 2))
        step -= (stepsize / 100)
    log("Count of ratios: " + str(len(array)))
    log("Ratios: " + json.dumps([round(i * 100, 0) for i in array]))
    return array


def interpolate_colors(start: dict, end: dict, ratio: float) -> dict:
    all_filaments = set(start.keys()) | set(end.keys())
    result = {}
    for f in all_filaments:
        p = start.get(f, 0.0) * ratio + end.get(f, 0.0) * (1.0 - ratio)
        if p > 0:
            result[f] = p
    return result


def generatepattern(proportions: dict, length: int, errors: dict) -> tuple:
    result = []
    filaments = [f for f, p in proportions.items() if p > 0]
    for _ in range(length):
        for f in filaments:
            errors[f] = errors.get(f, 0.0) + proportions[f]
        chosen = max(filaments, key=lambda f: errors.get(f, 0.0))
        result.append(str(chosen))
        errors[chosen] -= 1.0
    return "".join(result), errors


def generategradient(start: dict, end: dict, size: int, offset: int, ratiostepsize: int, lowerbound: int, upperbound: int) -> str:
    ratios = getratioarray(ratiostepsize, lowerbound, upperbound)
    patterns = []
    errors = {}
    gradient_size = max(0, size - offset)
    log("Amount of layers per ratio: " + str(gradient_size // len(ratios)) + " (±1 to distribute remainder)")

    if offset > 0:
        pattern, errors = generatepattern(start, offset, errors)
        patterns.append(pattern)

    for i, ratio in enumerate(ratios):
        proportions = interpolate_colors(start, end, ratio)
        layers = (i + 1) * gradient_size // len(ratios) - i * gradient_size // len(ratios)
        pattern, errors = generatepattern(proportions, layers, errors)
        patterns.append(pattern)

    return "".join(patterns)


print('Colors can be a single filament ("1") or a mix ("1:80,2:20" for 80% F1 + 20% F2).')
gradientstart = parse_color(input('Enter start color: '))
gradientend = parse_color(input('Enter end color: '))
size = int(input('Enter size/layers of gradient (int): '))

lowerbound = input('Enter lower mixing bound, defaults to 0% (int): ')
try:
    lowerbound = int(lowerbound) if int(lowerbound) > 0 else 0
except:
    lowerbound = 0

upperbound = input('Enter upper mixing bound, defaults to 100% (int): ')
try:
    upperbound = int(upperbound) if int(upperbound) < 100 else 100
except:
    upperbound = 100

gradientoffset = input('Enter offset in layers from the bottom, defaults to 0 (int): ')
try:
    gradientoffset = int(gradientoffset) if int(gradientoffset) > 0 else 0
except:
    gradientoffset = 0

smallgradient = input('Enter gradient stepsize, defaults to 5% (int): ')
try:
    smallgradient = int(smallgradient) if int(smallgradient) >= 0 else 5
except:
    smallgradient = 5

log("Start color: " + json.dumps(gradientstart))
log("End color: " + json.dumps(gradientend))

print('')
gradient = generategradient(gradientstart, gradientend, size, gradientoffset, smallgradient, lowerbound, upperbound)
print('')
print('Output:')
print(gradient)

input()
