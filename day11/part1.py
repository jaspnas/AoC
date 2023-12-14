from itertools import islice


with open("input.txt") as f:
    lines = [[x for x in l] for l in f.read().splitlines()]

z = iter(enumerate(lines))
for idy, line in z:
    if len([x for x in line if x != "."]) == 0:
        lines.insert(idy, line)
        list(islice(z, 2))

print(len(lines))

idx = 0
while idx < len(lines[0]):
    if len([line[idx] for line in lines if line[idx] != "."]) == 0:
        for line in lines:
            line.insert(idx, line[idx])
        idx += 2
    idx += 1

print(len(lines[0]))
        

point = []

for idy in range(len(lines)):
    for idx in range(len(lines[idy])):
        if lines[idy][idx] == "#":
            point.append((idy, idx))

s = 0
for i, a in enumerate(point):
    for b in point[i+1:]:
        s += abs(a[1]-b[1]) + abs(a[0]-b[0])

print(s)
