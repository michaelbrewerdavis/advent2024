import re


def parse(lines):
    return "".join(lines)


def part1(input):
    total = 0
    matches = re.findall(r"mul\((\d+),(\d+)\)", input)
    for a, b in matches:
        total += int(a) * int(b)
    return total


def part2(input):
    enabled = True
    matches = re.findall(r"(do\(\))|(don't\(\))|mul\((\d+),(\d+)\)", input)

    total = 0
    for do, dont, a, b in matches:
        if do != "":
            enabled = True
        elif dont != "":
            enabled = False
        elif enabled:
            total += int(a) * int(b)
    return total


def run(input):
    print(part1(input))
    print(part2(input))
