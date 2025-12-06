def part_1():
    total = 0
    with open("input.txt", "r", encoding="utf-8") as f:
        for line in f.read().splitlines():
            digits = list(map(int, line))
            max_1 = 0
            max_2 = 0
            max_1 = max(digits)
            i = digits.index(max_1)
            if i < len(digits) - 1:
                max_2 = max(digits[i + 1 :])
            else:
                max_2 = max_1
                max_1 = max(digits[:i])
            total += (max_1 * 10) + max_2
    print(total)


def max_12_digits(s, k_in):
    # will also work for part 1 if desired.
    digits = list(map(int, s))
    stack = []
    # must remove these many digits to have k_in digits left
    remove = len(digits) - k_in

    for d in digits:
        # while stack not empty, still digits to remove, and current digit larger than last chosen
        while stack and remove and (stack[-1] < d):
            print(f"A_Stack: {(stack)}, d: {d} To remove: {remove}")
            stack.pop()
            remove -= 1
            print(f"B_Stack: {(stack)}, d: {d} To remove: {remove}")
        stack.append(d)
        print(f"C_Stack: {stack}, d: {d} To remove: {remove}")

    return "".join(map(str, stack[:k_in]))


def part_2():
    total = 0
    with open("input.txt", "r", encoding="utf-8") as f:
        for line in f.read().splitlines():
            max_digits = max_12_digits(line, 12)
            total += int(max_digits)
    print(total)


if __name__ == "__main__":
    part_1()
    part_2()
