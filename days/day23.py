energies = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}


def part1():
    #             01234567890
    grid = [list("..........."),
            list("##B#B#D#A##"),
            list("##D#C#A#C##")]
    count = 0
    count += move(grid, (1, 8), (0, 9))
    count += move(grid, (2, 8), (0, 5))
    count += move(grid, (1, 6), (2, 8))
    count += move(grid, (2, 6), (0, 7))
    count += move(grid, (0, 5), (2, 6))
    count += move(grid, (1, 4), (0, 3))
    count += move(grid, (2, 4), (1, 6))
    count += move(grid, (0, 3), (2, 4))
    count += move(grid, (1, 2), (1, 4))
    count += move(grid, (0, 7), (0, 1))
    count += move(grid, (2, 2), (1, 8))
    count += move(grid, (0, 1), (2, 2))
    count += move(grid, (0, 9), (1, 2))
    print(count)


def part2():
    #             01234567890
    grid = [list("..........."),
            list("##B#B#D#A##"),
            list("##D#C#B#A##"),
            list("##D#B#A#C##"),
            list("##D#C#A#C##")]
    count = 0
    count += move(grid, (1, 2), (0, 0))
    count += move(grid, (2, 2), (0, 1))
    count += move(grid, (3, 2), (0, 10))
    count += move(grid, (4, 2), (0, 9))
    count += move(grid, (1, 8), (4, 2))
    count += move(grid, (2, 8), (3, 2))
    count += move(grid, (3, 8), (0, 3))
    count += move(grid, (4, 8), (0, 5))
    count += move(grid, (0, 9), (4, 8))
    count += move(grid, (0, 10), (3, 8))
    count += move(grid, (1, 6), (2, 8))
    count += move(grid, (2, 6), (0, 10))
    count += move(grid, (3, 6), (0, 9))
    count += move(grid, (4, 6), (0, 7))
    count += move(grid, (0, 5), (4, 6))
    count += move(grid, (0, 3), (3, 6))
    count += move(grid, (0, 7), (2, 2))
    count += move(grid, (0, 9), (1, 2))
    count += move(grid, (0, 1), (1, 8))
    count += move(grid, (1, 4), (0, 1))
    count += move(grid, (2, 4), (2, 6))
    count += move(grid, (3, 4), (0, 3))
    count += move(grid, (4, 4), (1, 6))
    count += move(grid, (0, 0), (4, 4))
    count += move(grid, (0, 1), (3, 4))
    count += move(grid, (0, 3), (2, 4))
    count += move(grid, (0, 10), (1, 4))
    print(count)


def move(grid, start, end):
    sx, sy = start
    ex, ey = end
    grid[ex][ey] = grid[sx][sy]
    grid[sx][sy] = '.'
    print_grid(grid)
    dis = sx + ex + abs(ey - sy)
    return dis * energies[grid[ex][ey]]


def print_grid(grid):
    for r in grid:
        print("".join(r))
    print("------------------------------")
