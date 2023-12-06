import re
from functools import reduce

with open("input.txt", "r") as f:
    lines = f.readlines()

convlines = [int("".join(re.findall(r"[0-9]+", x))) for x in lines]

print(convlines)

margin = 0
time = convlines[0]
dtb = convlines[1]
for i in range(time):
    total_distance = (time-i)*i
    if total_distance > dtb:
        margin += 1


print(margin)
