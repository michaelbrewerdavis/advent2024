def parse(input):
    return [list(map(int, line.strip().split(" "))) for line in input]

def is_safe(line):
    last = None
    dir = None

    for num in line:
        if last is None:
            pass
        else:
            if last == num:
                return False
            elif abs(last - num) > 3:
                return False
            
            if dir is None:
                if last > num:
                    dir = "decreasing"
                else:
                    dir = "increasing"
            else:
                if last > num and dir == "increasing":
                    return False
                if last < num and dir == "decreasing":
                    return False
                        
        last = num
    return True

def is_safe_with_problem_dampener(line: list[int]) -> bool:
    if is_safe(line):
        return True
    else:
        for i in range(len(line)):
            copy = line[::]
            del copy[i]
            if is_safe(copy):
                return True
    return False

def run(input):
    results1 = [is_safe(line) for line in input]
    print(results1.count(True))
    results2 = [is_safe_with_problem_dampener(line) for line in input]
    print(results2.count(True))
