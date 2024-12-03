import re
from shapely import Polygon, Point

pipematch = re.compile(r"(-|\||F|L|7|J)")

with open("input.txt", "r") as f:
    lines = f.read().splitlines()

for idy in range(len(lines)):
    for idx in range(len(lines[idy])):
        if lines[idy][idx] == "S":
            start = (idy, idx)

def find_next(last_pos, cur_pos):
    cur_y, cur_x = cur_pos[0], cur_pos[1]
    cur_val = lines[cur_y][cur_x]
    for l in [(cur_y-1, cur_x), (cur_y+1, cur_x), (cur_y, cur_x-1), (cur_y, cur_x+1)]:
        if l == last_pos:
            continue
        idy, idx = l[0], l[1]
        try:
            val = lines[idy][idx]
        except IndexError as err:
            continue
        if not pipematch.match(val):
            continue
        if val == "-" and (cur_y != idy or not ((cur_val in "FLS" and idx > cur_x) or (cur_val in "J7S" and idx < cur_x) or cur_val == "-")):
            continue
        if val == "|" and (cur_x != idx or not ((cur_val in "F7S" and idy > cur_y) or (cur_val in "JLS" and idy < cur_y) or cur_val == "|")):
            continue
        if val == "L" and not ((idy > cur_y and cur_val in "|F7S") or (idx < cur_x and cur_val in "-J7S")):
            continue
        if val == "F" and not ((idy < cur_y and cur_val in "|JLS") or (idx < cur_x and cur_val in "-7JS")):
            continue
        if val == "7" and not ((idy < cur_y and cur_val in "|LJS") or (idx > cur_x and cur_val in "-FLS")):
            continue
        if val == "J" and not ((idy > cur_y and cur_val in "|F7S") or (idx > cur_x and cur_val in "-FLS")):
            continue
        return l

    return start

values = [(-1, -1), start]

while lines[values[-1][0]][values[-1][1]] != "S" or len(values) < 3:
    values.append(find_next(values[-2], values[-1]))

values = values[1:]

area = Polygon(values)

s = 0

for idy in range(len(lines)):
    for idx in range(len(lines[idy])):
        p = Point([idy, idx])
        if p.within(area):
            s += 1

print(s)

