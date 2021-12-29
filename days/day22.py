import collections
import re
from collections import defaultdict


def get_input():
    ptn = re.compile(r"([^ ]+) x=([-]?\d+)\.\.([-]?\d+),y=([-]?\d+)\.\.([-]?\d+),z=([-]?\d+)\.\.([-]?\d+)")
    fobj = open("input/day22.txt")
    lines = fobj.readlines()
    fobj.close()
    ops = []
    for l in lines:
        gp = ptn.search(l.strip('\n')).groups()
        ops.append((gp[0], (int(gp[1]), int(gp[2])), (int(gp[3]), int(gp[4])), (int(gp[5]), int(gp[6]))))
    # (action, (x...), (y...), (z...))
    return ops


# inspired by https://stackoverflow.com/a/66370641/2741395
def parse_axis(l: list, limit):
    # need to merge points with same value
    ps = defaultdict(list)
    for i in range(len(l)):
        if -limit <= l[i][0] <= limit:
            ps[l[i][0]].append((i, True))
            ps[l[i][1]].append((i, False))
    ps = collections.OrderedDict(sorted(ps.items()))
    # (steps, (start, end))
    subs = []
    ids = set()
    open_value = None
    for p, acs in ps.items():
        to_add = None
        # points before this one
        if open_value is not None and p - 1 >= open_value:
            to_add = (set(ids), (open_value, p - 1))
            open_value = None

        # this point
        no_new_start = True
        for step, start in acs:
            if start:
                no_new_start = False
                ids.add(step)

        if to_add is not None and no_new_start:
            # include this one to previous
            subs.append((to_add[0], (to_add[1][0], p)))
            to_add = None
        elif to_add is not None:
            subs.append(to_add)
            to_add = (set(ids), (p, p))
        else:
            to_add = (set(ids), (p, p))

        # points after this one
        no_old_close = True
        for step, start in acs:
            if not start:
                no_old_close = False
                ids.discard(step)

        if to_add is not None and no_old_close and ids:
            # include this one to next
            open_value = p
        elif to_add is not None:
            subs.append(to_add)
            open_value = p + 1 if ids else None
        else:
            open_value = p + 1 if ids else None

    return subs


def count_cuboid(psx, psy, psz, actions):
    count = 0
    for x_steps, (x_start, x_end) in psx:
        for y_steps, (y_start, y_end) in psy:
            c_xy = set.intersection(x_steps, y_steps)
            if c_xy:
                for z_steps, (z_start, z_end) in psz:
                    c_xyz = set.intersection(c_xy, z_steps)
                    if c_xyz and actions[max(c_xyz)]:
                        n = (x_end - x_start + 1) * (y_end - y_start + 1) * (z_end - z_start + 1)
                        count += n
    return count


def prepare_input():
    ins = get_input()
    actions = {}
    ss = [[] for i in range(3)]
    for i in range(len(ins)):
        actions[i] = ins[i][0] == 'on'
        for j in range(3):
            ss[j].append(ins[i][j + 1])
    return actions, ss


def part1():
    limit = 50
    actions, ss = prepare_input()
    count = count_cuboid(*[parse_axis(l, limit) for l in ss], actions)
    print(count)


def part2():
    limit = 9999999
    actions, ss = prepare_input()
    count = count_cuboid(*[parse_axis(l, limit) for l in ss], actions)
    print(count)
