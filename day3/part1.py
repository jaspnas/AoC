import re
from itertools import islice

nums = re.compile("[0-9]")

with open("input.txt", "r") as f:
    input = f.readlines()

s = 0

for idy, line in enumerate(input):
    z = iter(enumerate(line))
    for idx, char in z:
        if nums.match(char):
            full_num = ""
            for i in range(idx, len(line)):
                if nums.match(line[i]):
                    full_num += line[i]
                else:
                    break
            add = False
            for l in range(idy-1, idy+2):
                for c in range(idx-1, idx+len(full_num)+1):
                    try:
                        x = input[l][c]
                        if x != "." and not nums.match(x) and x != "\n":
                            print(full_num, l, c, x)
                            add = True
                    except IndexError:
                        pass
            if add:
                s += int(full_num)
            list(islice(z, len(full_num)))

print(s)
