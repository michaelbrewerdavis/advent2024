def parse(lines):
    return list(map(int, lines[0].split(" ")))


def blink1(n):
    if n == 0:
        return [1]
    elif (l := len(s := str(n))) % 2 == 0:
        return [int(s[0 : l // 2]), int(s[l // 2 :])]
    else:
        return [n * 2024]


def countWithMultiple(acc, values, count):
    for v in values:
        c = acc.get(v, 0)
        acc[v] = c + count
    return acc


def blink(counts):
    newCounts = {}
    for key in counts:
        countWithMultiple(newCounts, blink1(key), counts[key])
    return newCounts


def run(input):
    counts = countWithMultiple({}, input, 1)
    for _ in range(25):
        counts = blink(counts)
    print(sum(counts.values()))

    for _ in range(50):
        counts = blink(counts)
    print(sum(counts.values()))
