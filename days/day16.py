from functools import reduce


def get_input():
    fobj = open("input/day16.txt")
    data = fobj.readline().strip('\n')
    fobj.close()
    return data


m = {"0": "0000", "1": "0001", "2": "0010", "3": "0011",
     "4": "0100", "5": "0101", "6": "0110", "7": "0111",
     "8": "1000", "9": "1001", "A": "1010", "B": "1011",
     "C": "1100", "D": "1101", "E": "1110", "F": "1111"}


def to_binary(data):
    l = []
    for c in data:
        l.extend(list(m[c]))
    return l


def bints_to_bint(data: list):
    return int("".join(data), 2)


def bints_to_dstr(data: list):
    return str(bints_to_bint(data))


def decode(data: list, s: int, vs: list):
    version = data[s: s+3]
    vs.append(version)
    s += 3
    type_id = data[s: s+3]
    s += 3

    ss = 0
    t = "".join(type_id)
    if "100" == t:
        ss, s = process_literal(data, s)
    else:
        l_id = data[s]
        s += 1
        l = []
        if l_id == '0':
            len_sub = bints_to_bint(data[s: s + 15])
            s += 15
            current = s
            while s < current + len_sub:
                ss, s = decode(data, s, vs)
                l.append(ss)
        elif l_id == '1':
            num_pack = bints_to_bint(data[s: s + 11])
            s += 11
            for i in range(num_pack):
                ss, s = decode(data, s, vs)
                l.append(ss)
        if '000' == t:
            ss = sum(l)
        elif '001' == t:
            ss = reduce(lambda x, y: x * y, l, 1)
        elif '010' == t:
            ss = min(l)
        elif '011' == t:
            ss = max(l)
        elif '101' == t:
            ss = 1 if l[0] > l[1] else 0
        elif '110' == t:
            ss = 1 if l[0] < l[1] else 0
        elif '111' == t:
            ss = 1 if l[0] == l[1] else 0

    return ss, s


def process_literal(data: list, s: int):
    i = s
    l = []
    while data[i] == '1':
        i += 1
        l.extend(data[i: i + 4])
        i += 4
    i += 1
    l.extend(data[i: i + 4])
    return int(bints_to_dstr(l)), i + 4


def part():
    vs = []
    ss, s = decode(to_binary(get_input()), 0, vs)
    vs = [int(bints_to_dstr(i)) for i in vs]
    return sum(vs), ss
