from collections import defaultdict
import itertools
import numpy as np

def match_ticket_fields(tickets, invalid_tickets, fields):
    valid_tickets = np.array([ticket for ix, ticket in enumerate(tickets) if ix not in [ticket[1] for ticket in invalid_tickets]], dtype = int)

    field_to_col = defaultdict(int)
    matched_fields = set()
    remaining_cols = set(range(0, len(fields)))

    while len(remaining_cols) != 0:
        for col in remaining_cols:
            is_field_OK = [all(value in criteria for value in valid_tickets[:, col]) for criteria in fields.values()]
            OK_fields = list(set(np.argwhere(is_field_OK).flatten()) - matched_fields)

            if len(OK_fields) == 1:
                matched_fields.add(OK_fields[0])
                remaining_cols.remove(col)
                field_to_col[OK_fields[0]] = col
                break

    return field_to_col

with open("Day_16/input.txt", "r") as fin:
    input = fin.read().split("\n\n")

    fields = defaultdict(set)
    for line in input[0].strip().split("\n"):
        field, rules = line.strip().split(": ")
        fields[field] = set(itertools.chain(*[range(int(rule.split("-")[0]), int(rule.split("-")[1])+1) for rule in rules.split(" or ")]))

    my_ticket = [int(value) for value in input[1].strip().split("\n")[1].split(",")] 
    tickets = np.array([[int(value) for value in ticket.split(",")] for ticket in input[2].strip().split("\n")[1:]], dtype = int)


# Day 16.1
invalid_tickets = [(value, ix) for ix, ticket in enumerate(tickets) for value in ticket if not any(value in criteria for criteria in fields.values())]
print(sum([ticket[0] for ticket in invalid_tickets]))

# Day 16.2
field_to_col = match_ticket_fields(tickets, invalid_tickets, fields)
print(np.prod([my_ticket[field_to_col[i]] for i, field in enumerate(fields.keys()) if field.startswith("departure")]))
