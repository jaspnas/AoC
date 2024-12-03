col1 = []
col2 = []

with open("input.txt", "r") as f:
    for line in f:
        col1.append(line.split("   ")[0])
        col2.append(line.split("   ")[1])

col1 = sorted(col1)
col2 = sorted(col2)

sum = 0

for i, _ in enumerate(col1):
    sum += abs(int(col1[i]) - int(col2[i]))

print(sum)
