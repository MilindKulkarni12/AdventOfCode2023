with open('./input.txt', 'r') as r:
    data = r.readlines()


def part1(cards):
    card_to_matches = {}
    total_points = 0
    for i, card in enumerate(cards):
        _, card_values = card.split(':', 1)
        winning_cards, our_cards = card_values.split('|')
        winning_cards = {k: True for k in winning_cards.split()}
        card_matches = 0

        for curr_card in our_cards.split():
            try:
                if winning_cards[curr_card]:
                    card_matches += 1
            except KeyError:
                continue
        points = 2 ** (card_matches - 1) if card_matches > 0 else 0
        total_points += points
        card_to_matches[i] = card_matches

    return total_points, card_to_matches


def part2(card_to_matches, n):
    new_mappings = {n: 1}
    i = n-1
    while i >= 0:
        count = 1
        count += sum([new_mappings[j] for j in range(i+1, i+card_to_matches[i]+1)])
        new_mappings[i] = count
        i -= 1
    print(new_mappings)
    return sum(new_mappings.values())


_, card_to_matches = part1(data)
# print(_, card_to_matches)
print(part2(card_to_matches, len(card_to_matches)-1))
