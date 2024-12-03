from functools import cmp_to_key
import re

pattern = re.compile(r"([0-9]|T|J|Q|K|A)")

conversions = {"T": 10, "J": 1, "Q": 12, "K": 13, "A": 14}

hands = []


def hand_value(hand: list):
    score = 0
    uniques = len(set(hand))
    if uniques == 5:
        score = 1
    elif uniques == 1:
        score = 7
    elif uniques == 2:
        if hand.count(hand[0]) in [4,1]:
            score = 6
        else:
            score = 5
    elif uniques == 3:
        if hand.count(max(set(hand), key=hand.count)) == 3:
            score = 4
        else: 
            score = 3
    else:
        score = 2
    
    return score


def joker_count(hand: list):
    results = []
    if hand.count(1) == 0:
        return hand_value(hand)
    for i in range(2,14):
        i = i+1 if i >10 else i
        hcopy = hand.copy()
        hcopy[hand.index(1)] = i
        results.append(joker_count(hcopy))
    return max(results)


def sorter(a, b):
    if a[2] != b[2]:
        return a[2]-b[2]
    for j, cc in enumerate(a[0]):
        if cc != b[0][j]:
            return cc - b[0][j]
    return 0
    
with open("input.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    hand, bid = [x.strip() for x in line.split(" ")]
    hand = [int(conversions.get(c, c)) for c in hand]
    hands.append((hand, bid, joker_count(hand)))

result = 0

for i, line in enumerate(sorted(hands, key=cmp_to_key(sorter))):
    print(i, line[0], line[2], line[1])
    result += (i+1) * int(line[1])

print(result)
