import copy


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

    def lower_collector(matrix: list[list], i: int, j: int, value: int):
        lows.append(value)

    find_lower(get_input(), lower_collector)
    print(lows)
    return sum(lows) + len(lows)


def part2():
    ss = []

    def flow(matrix: list[list], i: int, j: int, value: int):
        acc = []
        flow_rec(matrix, i, j, value, acc, set())
        ss.append(len(acc))

    def flow_rec(matrix: list[list], i: int, j: int, value: int, acc: list, visited: set):
        visited.add((i, j))
        adjacent = []
        # if i > 0 and matrix[i - 1][j] > value:
        #     adjacent.append((i-1, j, matrix[i - 1][j]))
        # if i < len(matrix) - 1 and matrix[i + 1][j] > value:
        #     adjacent.append((i+1, j, matrix[i + 1][j]))
        # if j > 0 and matrix[i][j - 1] > value:
        #     adjacent.append((i, j-1, matrix[i][j - 1]))
        # if j < len(matrix[i]) - 1 and matrix[i][j + 1] > value:
        #     adjacent.append((i, j+1, matrix[i][j + 1]))
        if i > 0 and matrix[i - 1][j] != 9:
            adjacent.append((i-1, j, matrix[i - 1][j]))
        if i < len(matrix) - 1 and matrix[i + 1][j] != 9:
            adjacent.append((i+1, j, matrix[i + 1][j]))
        if j > 0 and matrix[i][j - 1] != 9:
            adjacent.append((i, j-1, matrix[i][j - 1]))
        if j < len(matrix[i]) - 1 and matrix[i][j + 1] != 9:
            adjacent.append((i, j+1, matrix[i][j + 1]))

        if len(adjacent) > 0:
            acc.append(value)

        for (x, y, v) in adjacent:
            if not visited.__contains__((x, y)):
                flow_rec(matrix, x, y, v, acc, visited)

    find_lower(get_input(), flow)
    ss.sort(reverse=True)
    print(ss)
    return ss[0] * ss[1] * ss[2]
