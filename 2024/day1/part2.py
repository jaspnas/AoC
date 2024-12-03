col1 = []
col2 = []

with open("input.txt", "r") as f:
    for line in f.readlines():
        col1.append(line.split("   ")[0])
        col2.append(line.split("   ")[1].strip())

hist = {}
result = 0

for i in col2:
    if i in hist.keys():
        hist[i] += 1
    else:
        hist[i] = 1

#print(hist)

for i in col1:
    try:
        result += int(hist[i]) * int(i)
    except KeyError:
        result += 0

print(result) 
