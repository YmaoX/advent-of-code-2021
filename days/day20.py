def get_input():
    fobj = open("input/day20.txt")
    lines = fobj.readlines()
    fobj.close()
    algo = [0 if c == '.' else 1 for c in lines[0].strip('\n')]
    m = []
    for i in range(2, len(lines)):
        m.append([0 if c == '.' else 1 for c in lines[i].strip('\n')])

    return algo, m


def calculate(a, b, m, padding):
    s = ""
    for i in range(a - 1, a + 2):
        for j in range(b - 1, b + 2):
            if 0 <= i < len(m) and 0 <= j < len(m):
                s += str(m[i][j])
            else:
                s += str(padding)
    return s


def enhance(algo, m, t):
    i_i = m
    padding = 0
    for i in range(t):
        new_l = 2 + len(i_i)
        i_o = [[0] * new_l for i in range(new_l)]
        i_i = [[padding] * new_l, *[[padding] + l + [padding] for l in i_i], [padding] * new_l]
        for x in range(new_l):
            for y in range(new_l):
                i_o[x][y] = algo[int(calculate(x, y, i_i, padding), 2)]
        i_i = i_o
        padding = algo[int(str(padding) * 9, 2)]
    return i_i


def count_1(m):
    return sum([sum(i) for i in m])


def part(t):
    algo, m = get_input()
    i_o = enhance(algo, m, t)
    print(count_1(i_o))
