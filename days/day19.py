import re
from operator import itemgetter


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


def sort_beacons(l: list):
    # it's important to sort by all 3 values
    return sorted(l, key=itemgetter(0, 1, 2))


def match_multi(s1: list, s2: list, rn: int):
    ss2 = tuple(zip(*(rotate(i) for i in s2)))
    for j in ss2:
        sorted_s2 = sort_beacons(j)
        df = match_single(s1, sorted_s2, rn)
        if df is not None:
            new_s2 = []
            for v in sorted_s2:
                new_s2.append(tuple(a + b for a, b in zip(df, v)))
            return df, new_s2
    else:
        return None


def match_single(s1: list, s2: list, rn: int):
    # actually it's "total_length - (rn - 1) + 1"
    l1 = len(s1) - rn + 2
    l2 = len(s2) - rn + 2
    for i in range(l1):
        for j in range(l2):
            df = tuple(m - n for m, n in zip(s1[i], s2[j]))
            match = 1
            j_inner = j + 1
            for m in range(i + 1, len(s1)):
                for n in range(j_inner, len(s2)):
                    if len(s2) - n < rn - match:
                        break
                    elif tuple(m - n for m, n in zip(s1[m], s2[n])) == df:
                        match += 1
                        j_inner = n + 1
                        break
                if match == rn:
                    return df
    else:
        return None


def process_scanners():
    ss = get_input()
    ds = {}
    d = {}
    for i in range(len(ss)):
        d[i] = True if i == 0 else False
        ds[i] = sort_beacons(ss[i]) if i == 0 else ss[i]
    fixed = [0]
    scanners = [(0, 0, 0)]
    for i in fixed:
        for j in range(len(ss)):
            if not d[j]:
                res = match_multi(ds[i], ds[j], 12)
                if res is not None:
                    ds[j] = res[1]
                    scanners.append(res[0])
                    print(f"found scanner {j}: {res[0]}")
                    d[j] = True
                    fixed.append(j)
                    if len(fixed) == len(ss):
                        return scanners, ds


def part():
    scanners, beacons = process_scanners()
    all_beacons = set()
    for l in beacons.values():
        all_beacons.update(l)
    print(f"found {len(beacons)} beacons")

    m = 0
    for i in range(len(scanners)):
        for j in range(len(scanners)):
            if i != j:
                m = max(m, abs(scanners[i][0] - scanners[j][0]) + abs(scanners[i][1] - scanners[j][1])
                        + abs(scanners[i][2] - scanners[j][2]))
    print(f"largest Manhattan distance: {m}")
