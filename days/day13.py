import re


def get_input():
    r = r"fold along ([xy])=(\d+)"
    fs = []
    ts = []
    with open("input/day13.txt") as fo:
        f_i = False
        m_x = 0
        m_y = 0
        for line in fo:
            cs = line.strip('\n')
            if not cs:
                f_i = True
            elif f_i:
                gp = re.search(r, cs).groups()
                fs.append((gp[0], int(gp[1])))
            else:
                x, y = (int(i) for i in cs.split(","))
                m_x = max(x, m_x)
                m_y = max(y, m_y)
                ts.append((x, y))

    m = [[0] * (m_x + 1) for i in range(m_y + 1)]
    for i in ts:
        m[i[1]][i[0]] = 1

    return m, fs


def do_fold(m: list[list], f: tuple):
    p = f[1]
    if f[0] == 'x':
        r = [[0] * p for i in range(len(m))]
        for i in range(len(r)):
            for j in range(len(r[i])):
                j_j = 2 * p - j
                b = 0 if j_j >= len(m[i]) else m[i][j_j]
                r[i][j] = min(m[i][j] + b, 1)
    else:
        r = [[0] * len(m[0]) for i in range(p)]
        for i in range(len(r)):
            for j in range(len(r[i])):
                i_i = 2 * p - i
                b = 0 if i_i >= len(m) else m[i_i][j]
                r[i][j] = min(m[i][j] + b, 1)

    return r


def count_1(m: list[list]):
    c = 0
    for i in m:
        for j in i:
            if j == 1:
                c += 1
    return c


def part1():
    m, fs = get_input()
    m = do_fold(m, fs[0])
    return count_1(m)


def part2():
    m, fs = get_input()
    for f in fs:
        m = do_fold(m, f)
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 0:
                m[i][j] = " "
            else:
                m[i][j] = "#"
    for i in m:
        print("".join(i))
