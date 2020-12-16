from collections import defaultdict
import itertools
import numpy as np

def match_ticket_fields(tickets, fields):
    valid_tickets = np.array([ticket for ticket in tickets if all(any(value in criteria for criteria in fields.values()) for value in ticket)], dtype = int)
    
    field_to_col = defaultdict(int)
    while len(field_to_col) != len(fields):
        for col in [i for i in range(len(fields)) if i not in field_to_col.values()]:
            OK_fields = [i for i, criteria in enumerate(fields.values()) if i not in field_to_col.keys() and all(value in criteria for value in valid_tickets[:, col])]
            
            if len(OK_fields) == 1:
                field_to_col[OK_fields[0]] = col

    return field_to_col

with open("Day_16/input.txt", "r") as fin:
    input = fin.read().strip().split("\n\n")

    fields = defaultdict(set)
    for line in input[0].split("\n"):
        field, rules = line.split(": ")
        fields[field] = set(itertools.chain(*[range(int(rule.split("-")[0]), int(rule.split("-")[1])+1) for rule in rules.split(" or ")]))

    my_ticket = [int(value) for value in input[1].split("\n")[1].split(",")] 
    tickets = [[int(value) for value in ticket.split(",")] for ticket in input[2].split("\n")[1:]]


# Day 16.1
print(sum([value for ticket in tickets for value in ticket if not any(value in criteria for criteria in fields.values())]))

# Day 16.2
field_to_col = match_ticket_fields(tickets, fields)
print(np.prod([my_ticket[field_to_col[i]] for i, field in enumerate(fields.keys()) if field.startswith("departure")]))
