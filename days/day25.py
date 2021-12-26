def get_input():
    fobj = open("input/day25.txt")
    lines = fobj.readlines()
    fobj.close()
    return [list(l.strip('\n')) for l in lines]


def process(m: list):
    def get_west(i, j):
        y = len(m[i]) - 1 if j == 0 else j - 1
        return i, y

    def get_north(i, j):
        x = len(m) - 1 if i == 0 else i - 1
        return x, j

    def check(target, get_point):
        swap_list = []
        for i in range(len(m)):
            for j in range(len(m[i])):
                c = m[i][j]
                if '.' == c:
                    x, y = get_point(i, j)
                    if target == m[x][y]:
                        swap_list.append((i, j, x, y))
        return swap_list

    def swap(swap_list):
        for i, j, x, y in swap_list:
            m[i][j] = m[x][y]
            m[x][y] = '.'

    count = 0
    while True:
        l = check('>', get_west)
        changed = True if l else False
        swap(l)
        l = check('v', get_north)
        changed |= True if l else False
        swap(l)

        count += 1
        if not changed:
            print(count)
            break


def part1():
    process(get_input())
