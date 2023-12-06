import re

nums = re.compile(r"[0-9]+")

with open("input.txt", "r") as f:
    content = f.read()

mins = []

segments = list(reversed([list([[int(z) for z in nums.findall(y)] for y in x.splitlines()[1:]]) for x in content.split("\n\n")[1:]]))

seedranges = [int(x) for x in nums.findall(content.split("\n\n")[0])]

seedr = []

for i in range(0, len(seedranges), 2):
    seedr.append(range(seedranges[i], seedranges[i]+seedranges[i+1]))

i = 0

while True:
    var = i
    if i % 100000 == 0:
        print(f"i = {i}")
    for segment in segments:
        for line in segment:
            dstart, sstart, length = line
            if var in range(dstart, dstart+length):
                var += (sstart-dstart)
                break

    for r in seedr:
        if var in r:
            print(i, var)
            exit(0)

    i += 1
                
