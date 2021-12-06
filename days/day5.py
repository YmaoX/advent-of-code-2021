class Line(object):
    def __init__(self, t: tuple):
        self.x1 = t[0][0]
        self.y1 = t[0][1]
        self.x2 = t[1][0]
        self.y2 = t[1][1]

    def __str__(self):
        return f"(({self.x1}, {self.y1}), ({self.x2}, {self.y2}))"

    def __repr__(self):
        return self.__str__()

    def is_horizontal(self):
        return self.y1 == self.y2

    def is_vertical(self):
        return self.x1 == self.x2

    def mark(self, board: list):
        if self.is_vertical():
            step_y = +1 if self.y2 > self.y1 else -1
            for i in range(self.y1, self.y2 + step_y, step_y):
                board[self.x1][i] += 1
        elif self.is_horizontal():
            step_x = +1 if self.x2 > self.x1 else -1
            for i in range(self.x1, self.x2 + step_x, step_x):
                board[i][self.y1] += 1

    def mark2(self, board: list):
        self.mark(board)
        if not (self.is_vertical() or self.is_horizontal()):
            step_x = +1 if self.x2 > self.x1 else -1
            step_y = +1 if self.y2 > self.y1 else -1
            j = self.y1
            for i in range(self.x1, self.x2 + step_x, step_x):
                board[i][j] += 1
                j += step_y


def retrieve_lines():
    rtn = []
    with open("input/day5.txt") as fo:
        for line in fo:
            pos = line.strip("\n").split(" -> ")
            rtn.append(Line(tuple(map(lambda l: tuple(map(int, l.split(","))), pos))))
    return rtn


def count_board(board: list):
    count = 0
    for line in board:
        for point in line:
            if point >= 2:
                count += 1
    return count


def day5_1():
    lines = retrieve_lines()
    board = [[0] * 1000 for i in range(1000)]
    for line in lines:
        line.mark(board)
    return count_board(board)


def day5_2():
    lines = retrieve_lines()
    board = [[0] * 1000 for i in range(1000)]
    for line in lines:
        line.mark2(board)
    return count_board(board)
