def get_input():
    matrix = []
    with open("input/day9.txt") as fo:
        for line in fo:
            matrix.append([int(i) for i in line.strip("\n")])
    return matrix


def find_lower(matrix: list[list], callback):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            adjacent = []
            if i > 0:
                adjacent.append(matrix[i-1][j])
            if i < len(matrix) - 1:
                adjacent.append(matrix[i+1][j])
            if j > 0:
                adjacent.append(matrix[i][j-1])
            if j < len(matrix[i]) - 1:
                adjacent.append(matrix[i][j+1])
            for a in adjacent:
                if a <= matrix[i][j]:
                    break
            else:
                callback(matrix, i, j, matrix[i][j])


def part1():
    lows = []

    def lower_collector(matrix: list[list], i: int, j:int, value: int):
        lows.append(value)

    find_lower(get_input(), lower_collector)
    print(lows)
    return sum(lows) + len(lows)


