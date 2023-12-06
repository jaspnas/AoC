import re
from functools import reduce

with open("input.txt", "r") as f:
    lines = f.readlines()

convlines = [re.findall(r"[0-9]+", x) for x in lines]

races = [(int(convlines[0][i]), int(convlines[1][i])) for i in range(len(convlines[0]))]

print(races)

margins = []

for race in races:
    margin = 0
    time = race[0]
    dtb = race[1]
    for i in range(time):
        total_distance = (time-i)*i
        if total_distance > dtb:
            margin += 1

    margins.append(margin)

result = reduce(lambda x, y: x*y, margins)

print(result)
