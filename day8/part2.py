from math import lcm
import re


wordfinder = re.compile(r"\w+")

instridx = {
    "L": 0,
    "R": 1
}

mapdict = {}

def pathlen(x):
    l = 0
    while True:
        for inst in instructions:
            x = mapdict[x][instridx[inst]]
            l += 1
            if x.endswith("Z"):
                return l

with open("input.txt", "r") as f:
    lines = f.read().splitlines()

instructions = lines[0]

mapper = lines[2:]

for m in mapper:
    entries = wordfinder.findall(m)
    mapdict[entries[0]] = (entries[1], entries[2])

s = 0

loc = [x for x in [wordfinder.findall(m)[0] for m in mapper] if x.endswith("A")]

print(lcm(*[pathlen(l) for l in loc]))
