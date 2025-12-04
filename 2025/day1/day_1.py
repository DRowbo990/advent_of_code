import re

numbers = list(range(100))
num = 50
with open("input.txt", "r", encoding="utf-8") as f:
    # work with lines, not characters
    content = f.read().splitlines()
    result = []
    for line in content:
        m = re.match(r"([A-Za-z]+)(\d+)", line)
        if m:
            result.append(m.groups())
    for line in content:
        # use the current line and convert the numeric suffix to int safely
        if line and line[0] == "l":
            try:
                num = num + int(line[1:])
            except ValueError:
                # skip lines where the suffix is not a valid integer
                pass
