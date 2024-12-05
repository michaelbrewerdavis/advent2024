import math
import functools

def parse(input):
    rules_text, pages_text = "".join(input).split("\n\n")

    rules = {}
    for x, y in [rule.split("|") for rule in rules_text.split("\n")]:
        rules[x] = rules.get(x, set())
        rules[x].add(y)

    return (
        rules,
        [page.split(",") for page in pages_text.split("\n")],
    )

def isValid(rules, page_set):
    for i, page1 in enumerate(page_set):
        for page2 in page_set[i+1:]:
            if page1 in rules.get(page2, set()):
                return False
    return True

def middleNumber(ps):
    index = math.floor(len(ps)/2)
    return int(ps[index])

def fixPageSet(rules, ps):
    return sorted(ps, key=functools.cmp_to_key(
        lambda x, y: 1 if x in rules.get(y, set()) else -1
    ))

def run1(input):
    rules, page_sets = input
    valid_page_sets = [page_set for page_set in page_sets if isValid(rules, page_set)]
    middle_numbers = [middleNumber(ps) for ps in valid_page_sets]
    print(sum(middle_numbers))
 
def run2(input):
    rules, page_sets = input
    fixed = [fixPageSet(rules, ps) for ps in page_sets if not isValid(rules, ps)]
    middle_numbers = [middleNumber(ps) for ps in fixed]
    print(sum(middle_numbers))

def run(input):
    run1(input)
    run2(input)