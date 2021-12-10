from days.day7 import medians


def get_input():
    lines = []
    with open("input/day10.txt") as fo:
        for line in fo:
            lines.append(list(line.strip("\n")))
    return lines


pairs = {'{': '}', '[': ']', '(': ')', '<': '>'}
opens = set('{[(<')
closes = set('}])>')


#387363
def part1():
    scores = {'}': 0, ']': 0, ')': 0, '>': 0}
    for line in get_input():
        l = []
        for c in line:
            if opens.__contains__(c):
                l.append(c)
            else:
                last = l[-1]
                if pairs[last] != c:
                    scores[c] += 1
                    break
                l = l[:-1]
    return scores[')'] * 3 + scores[']'] * 57 + scores['}'] * 1197 + scores['>'] * 25137


#4330777059
def part2():
    scores = {'{': 3, '[': 2, '(': 1, '<': 4}
    all = []
    for line in get_input():
        l = []
        corrupted = False
        for c in line:
            if opens.__contains__(c):
                l.append(c)
            else:
                last = l[-1]
                if pairs[last] != c:
                    corrupted = True
                    break
                l = l[:-1]
        if not corrupted and len(l) > 0:
            l.reverse()
            total = 0
            for c in l:
                total = total * 5 + scores[c]
            all.append(total)
    return medians(all)
