def parse(input):
    return [list(map(int, line.strip().split('   '))) for line in input]

def distance(parsed):
    firsts = [x[0] for x in parsed]
    seconds = [x[1] for x in parsed]

    firsts.sort()
    seconds.sort()
    sorted = list(zip(firsts, seconds))

    return sum([abs(a - b) for a, b in sorted])


def similarity(parsed):
    firsts = [x[0] for x in parsed]
    seconds = [x[1] for x in parsed]

    counts = {}
    for val in seconds:
        counts[val] = counts.get(val, 0)
        counts[val] += 1
    
    score = 0
    for val in firsts:
        score += val * counts.get(val, 0)

    return score

def run(input):
    print(distance(input))
    print(similarity(input))