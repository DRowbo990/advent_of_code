total = 0
with open("input.txt", "r", encoding="utf-8") as f:
    content = f.read().split(",")
    for line in content:
        split = line.split("-")
        section = list(range(int(split[0]), int(split[1]) + 1))
        for _ in section:
            str_num = str(_)
            if len(str_num) % 2 == 0:
                str_length = len(str_num) // 2
                if str_num[:str_length] == str_num[str_length:]:
                    total += _
print(total)
# 857828578
