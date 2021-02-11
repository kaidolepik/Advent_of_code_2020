def combat(playerA, playerB):
    while playerA and playerB:
        cards = [playerA.pop(0), playerB.pop(0)]
        if cards[0] > cards[1]:
            playerA += cards
        else:
            playerB += cards[::-1]
    
    return playerA, playerB

def recursive_combat(playerA, playerB):
    game_states = set()

    while playerA and playerB:
        game_state = (tuple(playerA), tuple(playerB))
        if game_state in game_states:
            break
        game_states.add(game_state)

        cardA = playerA.pop(0)
        cardB = playerB.pop(0)
        if len(playerA) >= cardA and len(playerB) >= cardB:
            A, _ = recursive_combat(playerA[:cardA], playerB[:cardB])
            is_A_winner = len(A) > 0
        else:
            is_A_winner = cardA > cardB

        if is_A_winner:
            playerA += [cardA, cardB]
        else:
            playerB += [cardB, cardA]

    return playerA, playerB


with open("Day_22/input.txt", "r") as fin:
    playerA, playerB = [[int(card) for card in deck.split("\n")[1:]] for deck in fin.read().split("\n\n")]

# Day 22.1
A, B = combat(playerA.copy(), playerB.copy())
print(sum([(i + 1) * card for i, card in enumerate((A + B)[::-1])]))

# Day 22.2
A, B = recursive_combat(playerA.copy(), playerB.copy())
print(sum([(i + 1) * card for i, card in enumerate((A + B)[::-1])]))
