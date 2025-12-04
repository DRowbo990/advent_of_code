import re

numbers = list(range(100))
num = 50
count = 0
with open("input.txt", "r", encoding="utf-8") as f:
    content = f.read().splitlines()
    for line in content:
        if "L" in line:
            num -= int(re.findall(r"\d+", line)[0])
        elif "R" in line:
            num += int(re.findall(r"\d+", line)[0]) % 100
        num %= 100
        if num == 0:
            count += 1

print(count)
