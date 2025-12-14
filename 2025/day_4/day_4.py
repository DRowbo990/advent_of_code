def file_to_2d_matrix(filename):
    """
    Reads a file and converts its content into a 2D list of strings.
    """
    matrix = []
    try:
        with open(filename, "r") as file:
            for line in file:
                # Remove leading/trailing whitespace and split by delimiter
                char_list = [char for char in line.strip()]
                matrix.append(char_list)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return matrix


def part_1(data_matrix):
    rows = len(data_matrix)
    cols = len(data_matrix[0])

    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    count = 0
    for r in range(rows):
        for c in range(cols):
            if data_matrix[r][c] == "@":
                unreachable_count = 0

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        # Check if the neighboring cell is "@" or "X" so we dont miss already counted slots
                        if data_matrix[nr][nc] == "@" or data_matrix[nr][nc] == "X":
                            unreachable_count += 1

                if unreachable_count < 4:
                    data_matrix[r][c] = "X"
                    count += 1

    print(count)


def part_2(data_matrix):
    rows = len(data_matrix)
    cols = len(data_matrix[0])

    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    xcount_total = 0
    while True:
        holder = []
        for r in range(rows):
            for c in range(cols):
                if data_matrix[r][c] == "@":
                    unreachable_count = 0

                    for dr, dc in directions:
                        nr = r + dr
                        nc = c + dc
                        if 0 <= nr < rows and 0 <= nc < cols:
                            # Check if the neighboring cell is "@" so we dont miss already counted slots
                            if data_matrix[nr][nc] == "@":
                                unreachable_count += 1

                    if unreachable_count < 4:
                        holder.append((r, c))
        # print(holder)
        if holder == []:
            print(xcount_total)
            break
        for r, c in holder:
            data_matrix[r][c] = "."
            xcount_total += 1


if __name__ == "__main__":
    data_matrix = file_to_2d_matrix("input.txt")
    part_1(data_matrix)
    data_matrix = file_to_2d_matrix("input.txt")
    part_2(data_matrix)
