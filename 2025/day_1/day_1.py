import re

num = 50
count = 0
with open("input.txt", "r", encoding="utf-8") as f:
    content = f.read().splitlines()
    for line in content:
        number = int(re.findall(r"\d+", line)[0])
        if "L" in line:
            for i in range(number):
                num -= 1
                if num == 0:
                    count += 1
                if num < 0:
                    num = 99
        elif "R" in line:
            for i in range(number):
                num += 1
                if num > 99:
                    num = 0
                    count += 1
print(count)
