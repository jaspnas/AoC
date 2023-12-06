import re

nums = re.compile(r"[0-9]+")

with open("input.txt", "r") as f:
    content = f.read()

segments = content.split("\n\n")

seeds = [int(x) for x in nums.findall(segments[0])]

for segment in segments[1:]:
    lines = segment.split("\n")[1:]
    scopy = seeds.copy()
    for line in lines:
        dstart, sstart, length = [int(x) for x in nums.findall(line)]
        for i, val in enumerate(seeds):
            if val in range(sstart, sstart+length):
                scopy[i] += (dstart-sstart)
    seeds = scopy

print(min(seeds))
