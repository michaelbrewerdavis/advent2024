def parse(lines):
    def parseLine(line):
        lhs, rhs = line.split(": ")
        values = rhs.split(" ")
        return (int(lhs), list(map(int, values)))

    return list(map(parseLine, lines))


def isPossible(result, values, operators):
    def isPossibleN(result, partial, values):
        # print("check", result, partial, values)
        if len(values) == 0:
            return result == partial
        nextValue = values[0]
        try:
            return next(True for op in operators if isPossibleN(result, op(partial, nextValue), values[1:]))
        except StopIteration:
            return False
    return isPossibleN(result, values[0], values[1:])

def add(x, y):
    return x + y

def mult(x, y):
    return x * y

def join(x, y):
    return int(str(x) + str(y))

def run(input):
    print(sum(result for result, values in input if isPossible(result, values, [add, mult])))
    print(sum(result for result, values in input if isPossible(result, values, [add, mult, join])))
