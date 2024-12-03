import re

nums = re.compile(r"[0-9]*")

with open("input.txt", "r") as f:
    lines = f.readlines()

s = 0

for line in lines:
    res = 0
    _, data = line.split(":")
    cards, solutions = data.split("|")
    cardnums = nums.findall(solutions)
    solnums = nums.findall(cards)
    for card in cardnums:
        if card in solnums and card != "":
            res = max(res*2, 1)
    s += res

print(s)
