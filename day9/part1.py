import re

def predict_next(arr):
    newarr = [arr[i] - arr[i-1] for i in range(1, len(arr))]
    if len(set(newarr)) == 0 and arr[0] == 0:
       return 0
    return arr[-1] + predict_next(newarr)

nums = re.compile(r"-*\d+")

with open("input.txt", "r") as f:
    lines = [[int(i) for i in nums.findall(x)] for x in f.readlines()]

result = 0

for line in lines:
    result += predict_next(line)

print(result)