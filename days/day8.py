def get_input():
    def line_to_input(line: str):
        parts = line.strip("\n").split(" | ")
        return tuple(map(lambda p: p.split(" "), parts))

    fobj = open("input/day8.txt")
    lines = fobj.readlines()
    fobj.close()
    return tuple(map(line_to_input, lines))


def process_line(input: tuple, template: dict):
    m = process_signal(input[0])
    m = dict((m[k], k) for k in m)
    ds = ""
    for d in input[1]:
        s = set()
        for c in d:
            s.add(m.get(c))
        ds += template.get(frozenset(s))
    return int(ds)


def set_minus(a: str, b: str):
    return set(a) - set(b)


def set_to_str(s: set):
    return "".join(s)


def get_single(m: dict, l: int):
    return tuple(m.get(l))[0]


def process_signal(signal: list):
    """
    0 -> 6 (a b c e f g): d
    1 -> 2 (c f)
    2 -> 5 (a c d e g): b f
    3 -> 5 (a c d f g): b e
    4 -> 4 (b c d f)
    5 -> 5 (a b d f g): c e
    6 -> 6 (a b d e f g): c
    7 -> 3 (a c f)
    8 -> 7 (a b c d e f g)
    9 -> 6 (a b c d f g): e

    1, 4, 7, 8 is unique
    a = 7 - 1 = 3d - 2d
    (b d) = 4 - 1 = 4d - 2d
    (c d e) = (8 - 9) + (8 - 6) + (8 - 0) = 7d - 6d
        2 -> 5d same (a c d e)
    g = 2 - (a c d e)
        5 -> 5d same (a g b d)
    f = 5 - (a g b d)
    c = 1 - f = 2d - f
        3 -> 5d same (a c f g)
    d = 3 - (a c f g)
    b = (b d) - d
    e = the rest
    """
    # len - list of signal
    l_s_map = {}
    for sig in signal:
        l_s_map.setdefault(len(sig), set()).add(sig)

    # display - real
    w_s_map = {'a': set_to_str(set_minus(get_single(l_s_map, 3), get_single(l_s_map, 2)))}
    b_d = set_minus(get_single(l_s_map, 4), get_single(l_s_map, 2))
    c_d_e = set()
    for m in map(lambda s: set_minus(get_single(l_s_map, 7), set(s)), l_s_map.get(6)):
        c_d_e = c_d_e.union(m)

    c_d_e_a = c_d_e.union({w_s_map['a']})
    i_2 = set(tuple(filter(lambda l: c_d_e_a.issubset(set(l)), l_s_map.get(5)))[0])
    w_s_map['g'] = set_to_str(set_minus(i_2, c_d_e_a))

    a_g_b_d = b_d.union({w_s_map['a']}).union({w_s_map['g']})

    i_5 = set(tuple(filter(lambda l: a_g_b_d.issubset(set(l)), l_s_map.get(5)))[0])
    w_s_map['f'] = set_to_str(set_minus(i_5, a_g_b_d))
    w_s_map['c'] = set_to_str(set_minus(get_single(l_s_map, 2), {w_s_map['f']}))
    a_c_f_g = {w_s_map['a'], w_s_map['c'], w_s_map['f'], w_s_map['g']}
    i_3 = set(tuple(filter(lambda l: a_c_f_g.issubset(set(l)), l_s_map.get(5)))[0])
    w_s_map['d'] = set_to_str(set_minus(i_3, a_c_f_g))
    w_s_map['b'] = set_to_str(set_minus(b_d, {w_s_map['d']}))
    w_s_map['e'] = set_to_str(set_minus(set("abcdefg"), set(w_s_map.values())))

    return w_s_map


def part1():
    count = 0
    for t in get_input():
        for s in t[1]:
            if {2, 3, 4, 7}.__contains__(len(s)):
                count += 1
    print(count)


def part2():
    template = {}
    template[frozenset('abcefg')] = '0'
    template[frozenset('cf')] = '1'
    template[frozenset('acdeg')] = '2'
    template[frozenset('acdfg')] = '3'
    template[frozenset('bcdf')] = '4'
    template[frozenset('abdfg')] = '5'
    template[frozenset('abdefg')] = '6'
    template[frozenset('acf')] = '7'
    template[frozenset('abcdefg')] = '8'
    template[frozenset('abcdfg')] = '9'
    print(sum(map(lambda t: process_line(t, template), get_input())))
