import re

pattern = re.compile(r"(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))")


def str2num(s):
    return str({"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
               .get(s, s))


result = 0
with open("input.txt", "r") as f:
    for line in f.readlines():
        matches = pattern.findall(line)
        result += int(str2num(matches[0]) + str2num(matches[len(matches) - 1]))

print(result)
