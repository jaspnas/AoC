limits = {
    "red": 12,
    "blue": 14,
    "green": 13,
}

with open("input.txt", "r") as f:
    lines = f.readlines()

s = 0

for line in lines:
    idx, turns = tuple([x.strip() for x in line.split(":")])
    works = True
    for turn in turns.split(";"):
        for cards in turn.split(","):
            for amount, card in tuple([cards.strip().split(" ")]):
                if int(amount) > limits[card]:
                    works = False

    if works:
        s += int(idx.split(" ")[1])

print(s)
