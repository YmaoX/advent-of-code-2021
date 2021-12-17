import re


def get_input():
    r = r"target area: x=([-]?\d+)..([-]?\d+), y=([-]?\d+)..([-]?\d+)"
    fobj = open("input/day17.txt")
    line = fobj.readline().strip("\n")
    fobj.close()
    return tuple(int(i) for i in re.search(r, line).groups())


def get_vx_min(x_min):
    i = 0
    s = 0
    while s < x_min:
        i += 1
        s += i
    return i


def process_y(vy, vx_min, vx_max, x_min, x_max, y_min, y_max):
    s = h = t = 0
    v = vy
    found = []

    while True:
        t += 1
        s += v
        if v == 0:
            h = s
        if y_min <= s <= y_max:
            f = check_x(x_min, x_max, vx_min, vx_max, t)
            if f:
                found.extend(f)
        v -= 1
        if s < y_min:
            break

    h = h if found else 0
    return h, set((vx, vy) for vx in found)


def check_x(x_min, x_max, vx_min, vx_max, t):
    found = []
    for vx in range(vx_min, vx_max + 1):
        s = 0
        v = vx
        for i in range(t):
            s += v
            if s > vx_max:
                break
            if v > 0:
                v -= 1
        if x_min <= s <= x_max:
            found.append(vx)
    return found


def part():
    x_min, x_max, y_min, y_max = get_input()
    vx_min = get_vx_min(x_min)
    lh = []
    ss = set()
    # brute force, 200 is based on experiences
    for vy in range(y_min, 200):
        h, s = process_y(vy, vx_min, x_max, x_min, x_max, y_min, y_max)
        if h != 0:
            lh.append(h)
        if s:
            ss.update(s)

    print(max(lh))
    print(len(ss))
