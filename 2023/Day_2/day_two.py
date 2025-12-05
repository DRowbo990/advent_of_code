import re
from typing import List

# initialize the sum total
total = 0
# Opening a file in read mode
red = 0
green = 0
blue = 0
game = 0
with open("Day_2/games.txt", "r") as file:
    # read each line in the file
    for line in file:
        red = 0
        green = 0
        blue = 0
        game = 0
        x = 0
        # if line is there to strip
        if line.strip():
            splitter = line.split(";")
            for group in splitter:
                elements = group.split(",")
                for element in elements:
                    for char in element:
                        if char.isdigit():
                            if x > 0:
                                x *= 10
                                x += int(char)
                            else:
                                x += int(char)
                        elif char == "r":
                            red += x
                            x = 0
                        elif char == "g":
                            green += x
                            x = 0
                        elif char == "b":
                            blue += x
                            x = 0
                        elif char == ":":
                            game += x
                            x = 0
                        else:
                            pass
        print(red, green, blue, game)
        if red <= 12 and green <= 13 and blue <= 14:
            total += game
print("Part 1: " + str(total))


if __name__ == "__main__":
    pass
