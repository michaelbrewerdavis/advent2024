def parse(lines):
    top, bottom = "".join(lines).split("\n\n")
    regs = dict(zip(("A", "B", "C"), [int(line.strip().split(": ")[1]) for line in top.split("\n")]))
    program = list(map(int, bottom.strip().split(" ")[1].split(",")))

    return (regs, program)

def combo(arg, regs):
    if arg < 4:
        return arg
    elif arg == 4:
        return regs["A"]
    elif arg == 5:
        return regs["B"]
    elif arg == 6:
        return regs["C"]

def dv(arg, regs):
    n = regs["A"]
    d = pow(2, combo(arg, regs))
    return n // d

def runProgram(regs, program):
    # print(regs, program)
    ptr = 0
    output = []

    try:
        while True:
            op = program[ptr]
            arg = program[ptr+1]
            if op == 0:
                regs["A"] = dv(arg, regs)
            elif op == 1:
                regs["B"] = (regs["B"] ^ arg)
            elif op == 2:
                regs["B"] = combo(arg, regs) % 8
            elif op ==3:
                if regs["A"] != 0:
                    ptr = arg - 2
            elif op == 4:
                regs["B"] = (regs["B"] ^ regs["C"])
            elif op == 5:
                output.append(combo(arg, regs) % 8)
            elif op == 6:
                regs["B"] = dv(arg, regs)
            elif op == 7:
                regs["C"] = dv(arg, regs)
            # print(op, arg, regs, output)

            ptr += 2
    except IndexError:
        pass

    return output

def endsWith(short, long):
    sr = reversed(short)
    lr = reversed(long)
    for x, y in zip(sr, lr):
        if x != y:
            return False
    return True

def completes(x, program, length):
    if length == len(program):
        return x
    
    for i in range(8):
        n = x * 8 + i
        newRegs = {"A": 8 * x + i, "B": 0, "C": 0}
        newOutput = runProgram(newRegs, program)
        if newOutput == program[-length-1:]:
            y = completes(n, program, length+1)
            if y:
                return y
    return None


def run(input):
    (regs, program) = input
    print(",".join(map(str, runProgram(regs, program))))

    print(completes(0, program, 0))