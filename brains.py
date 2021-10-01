class Cell(object):
    def __init__(self, row, col, box, val):
        self.row = row
        self.col = col
        self.box = box
        self.val = val
        self.opt = [x for x in range(1, 10) if self.val == 0]


def main():
    # Uncomment to allow user input
    # cellstring = input("Please enter the values in one long string of text: ")

    # Uncomment for a test input
    cellstring = "800100000000003069000478030040000000000804103000000607500007008007600500000035090"

    grid = []
    for i, c in enumerate(cellstring):
        row = int(i / 9)
        col = int(i % 9)
        grid.append(Cell(row, col, (int(row / 3) * 3) + int(col / 3), int(c)))
    pre = 0
    new = countopt(grid)

    while pre != new:
        pre = new

        onlyval(grid)
        hiddensinglerows(grid)
        hiddensinglecols(grid)
        hiddensingleboxs(grid)
        possibles(grid)

        printgrid(grid)
        
        # For error checking to see what options each box should have available
        # printopts(grid)

        new = countopt(grid)


def countopt(grid):
    elements = []
    for x in grid:
        elements += x.opt

    return len(elements)


def onlyval(grid):
    for x in grid:
        if len(x.opt) == 1:
            x.val = x.opt.pop()
            x.opt = []
    possibles(grid)


def possibles(grid):
    for x in grid:
        for y in grid:
            if (x.row == y.row) or (x.col == y.col) or (x.box == y.box):
                if y.val in x.opt:
                    x.opt.remove(y.val)
                if x.val in y.opt:
                    y.opt.remove(x.val)


def hiddensinglerows(grid):
    for i  in range (0, 9):
        topossible = []
        elements = []
        for x in grid:
            if (x.row == i):
                elements+=x.opt
                topossible.append(x)
        for e in range (1, 10):
            if elements.count(e) == 1:
                for x in topossible:
                    if e in x.opt:
                        x.val = e
                        x.opt = []
    possibles(grid)


def hiddensinglecols(grid):
    for i  in range (0, 9):
        topossible = []
        elements = []
        for x in grid:
            if (x.col == i):
                elements+=x.opt
                topossible.append(x)
        for e in range (1, 10):
            if elements.count(e) == 1:
                for x in topossible:
                    if e in x.opt:
                        x.val = e
                        x.opt = []
    possibles(grid)


def hiddensingleboxs(grid):
    for i  in range (0, 9):
        topossible = []
        elements = []
        for x in grid:
            if (x.box == i):
                elements+=x.opt
                topossible.append(x)

        for e in range (1, 10):
            if elements.count(e) == 1:
                for x in topossible:
                    if e in x.opt:
                        x.val = e
                        x.opt = []
    possibles(grid)


def printgrid(grid):
    for i, x in enumerate(grid):
        if (i % 9 == 0) & (i != 0):
            print("|")

        if i % 27 == 0:
            print("-------------")

        if i % 3 == 0:
            print("|", end='')

        print(str(x.val), end='')

    print("|")
    print("-------------")
    print("")


def printopts(grid):
    for x in grid:
        print(x.opt)


if __name__ == "__main__":
    main()
