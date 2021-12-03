def find_most_least(numbers):
    base = []
    count = 0
    for line in numbers:
        int_list = [int(i) for i in list(line.rstrip('\n'))]
        if not base:
            base = [0] * len(int_list)

        base = [sum(x) for x in zip(base, int_list)]
        count += 1

    most = ""
    least = ""
    for x in base:
        if x < count / 2:
            most += "0"
            least += "1"
        else:
            most += "1"
            least += "0"
    return most, least, int(most, 2) * int(least, 2)


def day3_1():
    fobj = open("input/day3.txt")
    rtn = find_most_least(fobj.readlines())
    fobj.close()
    return rtn


def filter_lines(numbers, start_bits, pos, index):
    lines = list(filter(lambda line: list(line.rstrip('\n'))[pos] == start_bits[pos], numbers))
    if len(lines) == 1:
        print("found")
        return lines[0]

    return filter_lines(lines, find_most_least(lines)[index], pos+1, index)


def day3_2():
    fobj = open("input/day3.txt")
    lines = fobj.readlines()
    (most, least, multi) = find_most_least(lines)
    print("filter oxygen...")
    oxygen = filter_lines(lines, most, 0, 0)
    print("filter co2...")
    co2 = filter_lines(lines, least, 0, 1)
    fobj.close()
    return oxygen, co2, int(oxygen, 2) * int(co2, 2)
