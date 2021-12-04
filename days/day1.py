def day1_help(window_size):
    count = 0
    with open("input/day1.txt") as fo:
        w = []
        for line in fo:
            line_d = int(line)
            w.append(line_d)
            if len(w) == window_size + 1:
                if w[window_size] > w[0]:
                    count += 1
                w.pop(0)
    return count


def day1_1():
    return day1_help(1)


def day1_2():
    return day1_help(3)
