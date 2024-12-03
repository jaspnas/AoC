import re
with open("input.txt", "r") as f:
    print(sum([int(x[0] + x[len(x)-1]) for x in [re.findall(r"[0-9]", y) for y in f.readlines()]]))
