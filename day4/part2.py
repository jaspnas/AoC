import re

nums = re.compile(r"[0-9]*")

with open("input.txt", "r") as f:
    lines = f.readlines()


for line in lines:
    wins = 0
    cardinfo, data = line.split(":")
    cards, solutions = data.split("|")
    cardnums = nums.findall(solutions)
    solnums = nums.findall(cards)
    for card in cardnums:
        if card in solnums and card != "":
            lines.append(lines[int(cardinfo.split(" ")[-1])+wins])
            wins += 1

print(len(lines))
