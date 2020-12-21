import itertools
import re

def match_rules(rules, key):
    matches = []
    for rule in rules[key]:
        key_matches = [""]
        for key in rule:
            key_matches = [x + y for x, y in itertools.product(key_matches, match_rules(rules, key))] if key.isdigit() else [key]
        matches += key_matches

    return matches

def match_messages(messages, rules, max_loops_42 = 10, max_loops_31 = 10):
    rule_42 = match_rules(rules, "42")
    rule_31 = match_rules(rules, "31")
    
    regex = lambda i42, i31: r"^(" + "|".join(rule_42) + "){" + str(i42) + "}" + "(" + "|".join(rule_31) + "){" + str(i31) + "}$"
    loop_options = [(i + j, i) for i in range(1, max_loops_31 + 1) for j in range(1, max_loops_42 + 1)]

    return [message for message in messages if any(re.match(regex(i42, i31), message) for i42, i31 in loop_options)]


with open("Day_19/input.txt", "r") as fin:
    input = fin.read().replace('"', "").split("\n\n")

    rules = { line.split(": ")[0]: [rule.split() for rule in line.split(": ")[1].split(" | ")] for line in input[0].strip().split("\n") }
    messages = input[1].strip().split()

print(len(set(messages).intersection(set(match_rules(rules, "0"))))) # Day 19.1
print(len(match_messages(messages, rules))) # Day 19.2 (also solves Day 19.1 with "match_messages(messages, rules, 1, 1)")
