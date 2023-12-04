from functools import reduce
minimums = {
    "red": 0,
    "blue": 0,
    "green": 0,
}

with open("input.txt", "r") as f:
    lines = f.readlines()

s = 0

for line in lines:
    idx, turns = tuple([x.strip() for x in line.split(":")])
    cardmins = minimums.copy()
    for turn in turns.split(";"):
        for cards in turn.split(","):
            for amount, card in tuple([cards.strip().split(" ")]):
                if cardmins[card] < int(amount):
                    cardmins[card] = int(amount)

    s += reduce(lambda x, y: x*y, cardmins.values())

print(s)
