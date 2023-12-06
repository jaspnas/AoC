import re
import gc




nums = re.compile(r"[0-9]+")

with open("input.txt", "r") as f:
    content = f.read()

mins = []

segments = content.split("\n\n")

seedranges = [int(x) for x in nums.findall(segments[0])]

for i in range(0, len(seedranges), 2):
    seeds = range(seedranges[i], seedranges[i]+seedranges[i+1])

    print(f"Seed amount: {len(seeds)}")

    for segment in segments[1:]:
        lines = segment.split("\n")[1:]
        scopy = seeds.copy()
        for line in lines:
            dstart, sstart, length = [int(x) for x in nums.findall(line)]

        
        mins.append(min(seeds))

print(min(mins))
