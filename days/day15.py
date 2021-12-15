import operator


def get_input():
    fobj = open("input/day15.txt")
    lines = [l.strip('\n') for l in fobj.readlines()]
    fobj.close()
    return [list(map(int, list(l))) for l in lines]


def get_min(ns: dict):
    (i, j), k = min(ns.items(), key=operator.itemgetter(1))
    del ns[(i, j)]
    return (i, j), k


def process(m: list[list]):
    l = len(m)
    visited = init_array(l, 0)
    dis = init_array(l, 9999999)
    dis[0][0] = 0
    ns = {(0, 0): 0}
    while True:
        (i, j), v = get_min(ns)

        if i == l - 1 and j == l - 1:
            return v

        visited[i][j] = True

        for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= x < l and 0 <= y < l and not visited[x][y]:
                dis[x][y] = min(m[x][y] + v, dis[x][y])
                ns[(x, y)] = dis[x][y]


def to_full(m: list[list]):
    def grow(i: int):
        return 1 if i == 9 else i+1

    t = 4
    for line in m:
        ori = line
        for n in range(t):
            ori = [grow(i) for i in ori]
            line.extend(ori)
    ori = m
    new_m = []
    for n in range(t):
        n_ori = ori
        ori = []
        for line in n_ori:
            l = [grow(i) for i in line]
            new_m.append(l)
            ori.append(l)
    m.extend(new_m)
    return m


def init_array(l: int, v: int):
    return [[v] * l for i in range(l)]


def part1():
    return process(get_input())


def part2():
    return process(to_full(get_input()))
