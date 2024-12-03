import re


wordfinder = re.compile(r"\w+")

instridx = {
    "L": 0,
    "R": 1
}


with open("input.txt", "r") as f:
    lines = f.read().splitlines()

mapdict = {}

instructions = lines[0]

mapper = lines[2:]

for m in mapper:
    entries = wordfinder.findall(m)
    mapdict[entries[0]] = (entries[1], entries[2])

s = 0

loc = "AAA"
while True:
    for instr in instructions:
        loc = mapdict[loc][instridx[instr]]
        s += 1
        if loc == "ZZZ":
            print(s)
            exit()
        