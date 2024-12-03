import re
from itertools import islice

nums = re.compile("[0-9]")

with open("input.txt", "r") as f:
    inlines = f.readlines()


def num_start_idx(idy, idx):
    line = inlines[idy]
    while True:
        try:
            if nums.match(line[idx-1]):
                idx -= 1
            else:
                return idx
        except IndexError:
            return idx


def fullnumber(idy, idx):
    result = ""
    while True:
        x = inlines[idy][idx]
        if nums.match(x):
            result += x
            idx += 1
        else:
            return result


def getnumbers(idy, idx):
    """Get numbers next to symbol"""

    result = []

    for l in range(idy - 1, idy + 2):
        z = iter(range(idx - 1, idx + 2))
        for c in z:
            try:
                x = inlines[l][c]
                if nums.match(x):
                    num = fullnumber(l, num_start_idx(l, c))
                    result.append(num)
                    list(islice(z, len(fullnumber(l, c))-1))
            except IndexError:
                pass

    print(idy, idx, result)
    return result


s = 0

for yid, line in enumerate(inlines):
    for xid, char in enumerate(line):
        if char == "*":
            nmbrs = getnumbers(yid, xid)
            if len(nmbrs) == 2:
                s += int(nmbrs[0]) * int(nmbrs[1])

print(s)
