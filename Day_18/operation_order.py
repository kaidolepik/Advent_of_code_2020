import operator
import re
import math

operators = { "+": operator.add, "*": operator.mul }

def evaluate_basic(ops, nrs):
    total = operators[ops[0]](nrs[0], nrs[1])
    for op, nr in zip(ops[1:], nrs[2:]):
        total = operators[op](total, nr)
    
    return total

def evaluate_advanced(ops, nrs):
    while "+" in ops:
        i = ops.index("+")
        nrs.insert(i, nrs.pop(i) + nrs.pop(i))
        ops.pop(i)

    return math.prod(nrs)

def evaluate(expression, evaluate_func):
    ops = [op for op in re.split(r"\d", expression) if op != ""]
    nrs = [int(nr) for nr in re.split("[*+]", expression)]

    return str(evaluate_func(ops, nrs))

def solve(expression, evaluate_func):
    while expression.startswith("("):
        match = re.search(r'\(([0-9+*]+)\)', expression)
        expression = expression.replace(match.group(0), evaluate(match.group(1), evaluate_func))

    return int(expression)


with open("Day_18/input.txt") as fin:
    input = [line.strip().replace(" ", "") for line in fin]

print(sum([solve("(" + expression + ")", evaluate_basic) for expression in input])) # Day 18.1
print(sum([solve("(" + expression + ")", evaluate_advanced) for expression in input])) # Day 18.2
