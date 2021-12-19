import re


def get_input():
    ss = []
    with open("input/day19.txt") as fo:
        s = None
        for line in fo:
            if line.startswith("---"):
                if s:
                    ss.append(s)
                s = []
                continue
            l = line.strip('\n')
            if l:
                s.append(tuple(int(i) for i in l.split(',')))
        ss.append(s)
    return tuple(ss)


# fixing an axis, rotate clockwise
def roll(t: tuple):
    return t[0], t[2], -t[1]


# fixing top, rotate clockwise
def turn(t: tuple):
    return t[1], -t[0], t[2]


# given an axis on top, there are 4 possibilities
# and we can have positive and negative axis on top, so 6 possibilities
def rotate(t: tuple):
    l = []
    for cycle in range(2):
        for step in range(3):
            t = roll(t)
            l.append(t)
            for i in range(3):
                t = turn(t)
                l.append(t)
        t = roll(turn(roll(t)))
    return l


def match_multi(s1: list, s2: list):
    ss2 = tuple(zip(*(rotate(i) for i in s2)))
    for j in ss2:
        df = match_single(s1, j)
        if df is not None:
            print(f"scanner: {df}")
            new_s2 = []
            for v in j:
                new_s2.append(tuple(a + b for a, b in zip(df, v)))
            return new_s2
    else:
        return None


def match_single(s1: list, s2: list):
    for i in range(len(s1)):
        for j in range(len(s2)):
            df = tuple(m - n for m, n in zip(s1[i], s2[j]))
            match = {j: i}
            count = 1
            for m in range(len(s1)):
                for n in range(len(s2)):
                    if m != i and n not in match and tuple(m - n for m, n in zip(s1[m], s2[n])) == df:
                        match[n] = m
                        count += 1
                        break
                if count == 12:
                    return df
    else:
        return None


def part1():
    ss = get_input()
    ds = {}
    d = {}
    for i in range(len(ss)):
        d[i] = False
        ds[i] = ss[i]
    fixed = [0]
    d[0] = True
    while len(fixed) < len(ss):
        for i in fixed:
            for j in range(len(ss)):
                if not d[j]:
                    s2 = match_multi(ds[i], ds[j])
                    if s2 is not None:
                        ds[j] = s2
                        fixed.append(j)
                        d[j] = True
                        print(f"processed scanner {j}")
    all_scanners = set()
    for l in ds.values():
        all_scanners.update(l)
    print(len(all_scanners))


def part2():
    fobj = open("input/day19_res.txt")
    lines = fobj.readlines()
    fobj.close()
    r = re.compile("scanner: \(([-]?\d+), ([-]?\d+), ([-]?\d+)\), processed scanner (\d+)")
    scanners = [(0, 0, 0)]
    for line in lines:
        gps = r.search(line.strip("\n")).groups()
        scanners.append((int(gps[0]), int(gps[1]), int(gps[2])))
    print(scanners)

    m = 0
    for i in range(len(scanners)):
        for j in range(len(scanners)):
            if i != j:
                m = max(m, abs(scanners[i][0] - scanners[j][0]) + abs(scanners[i][1] - scanners[j][1])
                        + abs(scanners[i][2] - scanners[j][2]))
    print(m)
