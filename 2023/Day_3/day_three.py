arrays = []
tot = 0
sum_total = 0
row_num = 0
set_flag = False

with open("Day_3/parts.txt", "r", encoding="utf-8") as file:
    # read each line in the file
    for line in file:
        current_array = []  # Create a new array for each line
        for char in line:
            if char.isdigit() or char in ".-*/+%&@#$=":
                current_array.append(char)
        # print(current_array)
        row_num += 1
        arrays.append(current_array)
    # find numbers in the array by going element by element and see if there is a symbol in the array next to it
    for idx1, char in enumerate(arrays):
        for idx2, i in enumerate(char):
            if i.isdigit():
                if arrays[idx1][idx2].isdigit():
                    if tot == 0:
                        tot = int(i)
                    else:
                        tot = (tot * 10) + int(i)
                # right check
                if (idx2 + 1) < row_num and arrays[idx1][idx2 + 1] in "-*/+%&@#$=":
                    set_flag = True

                # left check
                elif arrays[idx1][idx2 - 1] in "-*/+%&@#$=":
                    set_flag = True

                # bottom check
                elif (idx1 + 1) < len(arrays) and arrays[idx1 + 1][
                    idx2
                ] in "-*/+%&@#$=":
                    set_flag = True

                # top left check
                elif arrays[idx1 - 1][idx2] in "-*/+%&@#$=" and idx1 - 1 >= 0:
                    set_flag = True

                # top right check
                elif (
                    (idx1 + 1) < len(arrays)
                    and (idx2 + 1) < row_num
                    and arrays[idx1 + 1][idx2 + 1] in "-*/+%&@#$="
                ):
                    set_flag = True

                # bottom right check
                elif (
                    (idx1 - 1) < len(arrays)
                    and (idx2 + 1) < row_num
                    and arrays[idx1 - 1][idx2 + 1] in "-*/+%&@#$="
                ):
                    set_flag = True

                # top left check
                elif (
                    (idx1 - 1) >= 0
                    and (idx2 - 1) >= 0
                    and arrays[idx1 - 1][idx2 - 1] in "-*/+%&@#$="
                ):
                    set_flag = True

                # bottom left check
                elif (
                    (idx1 + 1) < len(arrays)
                    and (idx2 - 1) >= 0
                    and arrays[idx1 + 1][idx2 - 1] in "-*/+%&@#$="
                ):
                    set_flag = True

                else:
                    if not set_flag:
                        set_flag = False

            elif i in ".-*/+%&@#$=" and set_flag:
                sum_total += tot
                tot = 0
                set_flag = False
            else:
                set_flag = False
                tot = 0
    print(sum_total)

if __name__ == "__main__":
    pass
