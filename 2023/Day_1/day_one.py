import re
from typing import List
from typing import List

open_file = "Day_1/test.txt"


def strip_num(line):
    result = re.findall(r"\d+", line)
    # merge all numbers into a single string
    result = "".join(result)
    return result


# initialize the sum total
total = 0
# Opening a file in read mode
with open("Day_1/seed.txt", "r") as file:
    # read each line in the file
    for line in file:
        # if line is there to strip
        if line.strip():
            # strip the line of anything other than integers
            num = strip_num(line)
            # get the first and last character of the line
            first_char = num[0]
            last_char = num[-1]
            # add the first and last character together
            num2 = (first_char) + (last_char)
            total = total + int(strip_num(num2))
    # print the total
    print("Part 1: " + str(total))

# initialize the sum total
total = 0
# Opening a file in read mode
with open("Day_1/seed.txt", "r") as file:
    # read each line in the file
    for line in file:
        # reset num array each loop to avoid adding previous numbers
        num = []
        # break line into individual characters and put in array
        for i in range(len(line)):
            if line[i] == "o":
                if line[i : i + 3] == "one":
                    num.append(1)
            elif line[i] == "t":
                if line[i : i + 3] == "two":
                    num.append(2)
                if line[i : i + 5] == "three":
                    num.append(3)
            elif line[i] == "f":
                if line[i : i + 4] == "four":
                    num.append(4)
                if line[i : i + 4] == "five":
                    num.append(5)
            elif line[i] == "s":
                if line[i : i + 3] == "six":
                    num.append(6)
                if line[i : i + 5] == "seven":
                    num.append(7)
            elif line[i] == "e":
                if line[i : i + 5] == "eight":
                    num.append(8)
            elif line[i] == "n":
                if line[i : i + 4] == "nine":
                    num.append(9)
            elif line[i] == "0":
                num.append(0)
            elif line[i] == "1":
                num.append(1)
            elif line[i] == "2":
                num.append(2)
            elif line[i] == "3":
                num.append(3)
            elif line[i] == "4":
                num.append(4)
            elif line[i] == "5":
                num.append(5)
            elif line[i] == "6":
                num.append(6)
            elif line[i] == "7":
                num.append(7)
            elif line[i] == "8":
                num.append(8)
            elif line[i] == "9":
                num.append(9)
            # if the line is a new line sum the first and last character
            elif line[i] == "\n":
                first_char = num[0] * 10
                last_char = num[-1]
                # add the first and last character together
                num2 = (first_char) + (last_char)
                total = total + (num2)
# sum the first and last character of the last line
first_char = num[0] * 10
last_char = num[-1]
# add the first and last character together
num2 = (first_char) + (last_char)
total = total + (num2)
print("Part 2: " + str(total))


if __name__ == "__main__":
    pass
