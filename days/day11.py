def get_input():
    matrix = []
    with open("input/day11.txt") as fo:
        for line in fo:
            matrix.append([int(i) for i in line.strip("\n")])
    return matrix


def increase(matrix: list[list]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] += 1


def flash(matrix: list[list], i, j):
    has_new = False
    for a in range(i-1, i+2):
        for b in range(j-1, j+2):
            if (i != a or j != b) \
                    and a >= 0 and b >= 0 and a < len(matrix) and b < len(matrix) \
                    and matrix[a][b] != 10 and matrix[a][b] != -1:
                matrix[a][b] += 1
                if matrix[a][b] == 10:
                    has_new = True
    matrix[i][j] = -1
    return has_new


def flash_all(matrix: list[list]):
    has_new = False
    count = 0
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] == 10:
                has_new |= flash(matrix, x, y)
                count += 1
    if has_new:
        count += flash_all(matrix)
    return count


def reset(matrix: list[list]):
    all_zero = True
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] == -1:
                matrix[x][y] = 0
            else:
                all_zero = False
    return all_zero


def part1():
    matrix = get_input()
    count = 0
    for i in range(100):
        increase(matrix)
        count += flash_all(matrix)
        reset(matrix)
    return count


def part2():
    matrix = get_input()
    count = 1
    while True:
        increase(matrix)
        flash_all(matrix)
        if reset(matrix):
            break
        count += 1
    return count
