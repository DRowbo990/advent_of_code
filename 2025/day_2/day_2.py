def part_1():
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


def is_repeating(s: str) -> bool:
    n = len(s)
    for size in range(1, n // 2 + 1):
        if n % size == 0:
            if s == s[:size] * (n // size):
                return True
    return False


def part_2():
    total = 0
    with open("input.txt", "r", encoding="utf-8") as f:
        content = f.read().split(",")

        for line in content:
            start, end = map(int, line.split("-"))
            for value in range(start, end + 1):
                if is_repeating(str(value)):
                    total += value

    print(total)


if __name__ == "__main__":
    part_1()
    part_2()
