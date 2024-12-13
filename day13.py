import re


def parse(lines):
    def parseBlock(block):
        aLine, bLine, prizeLine = [line.strip() for line in block.split("\n")]
        ax, ay = list(map(int, re.match(r"Button A: X+(.*), Y+(.*)", aLine).groups()))
        bx, by = list(map(int, re.match(r"Button B: X+(.*), Y+(.*)", bLine).groups()))
        prizex, prizey = list(
            map(int, re.match("Prize: X=(.*), Y=(.*)", prizeLine).groups())
        )
        return ((ax, ay), (bx, by), (prizex, prizey))

    return list(map(parseBlock, "".join(lines).split("\n\n")))


def solve(system):
    (a, c), (b, d), (X, Y) = system
    X = X + 10000000000000
    Y = Y + 10000000000000
    det = a * d - b * c
    if det == 0:
        return None
    ainv = d / det
    binv = -b / det
    cinv = -c / det
    dinv = a / det
    x = round(X * ainv + Y * binv)
    y = round(X * cinv + Y * dinv)
    if a * x + b * y == X and c * x + d * y == Y:
        return (x, y)


def run(input):
    tokens = 0
    for system in input:
        if (solution := solve(system)) is not None:
            a, b = solution
            tokens += 3 * a + b
    print(tokens)
