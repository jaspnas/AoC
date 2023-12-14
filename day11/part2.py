inserts = 1000000

def empty_lines_above(idy):
    s = 0
    for line in lines[:idy]:
        if len([x for x in line if x != "."]) == 0:
            s+=1
    return s*inserts-s

def empty_lines_left(idx):
    s = 0
    for x in range(idx):
        if len([line[x] for line in lines if line[x] != "."]) == 0:
            s += 1
    return s*inserts-s
        


with open("input.txt") as f:
    lines = [[x for x in l] for l in f.read().splitlines()]

point = []


for idy in range(len(lines)):
    for idx in range(len(lines[idy])):
        if lines[idy][idx] == "#":
            point.append((idy+empty_lines_above(idy), idx+empty_lines_left(idx)))

s = 0
for i, a in enumerate(point):
    for b in point[i+1:]:
        s += abs(a[1]-b[1]) + abs(a[0]-b[0])

print(s)
