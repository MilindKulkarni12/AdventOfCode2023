from collections import Counter
from functools import cmp_to_key

with open('./input.txt', 'r') as r:
    lines = r.readlines()


# card ranks part 1
card_ranks = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}

# card ranks part 2
card_ranks = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "T": 11,
    "9": 10,
    "8": 9,
    "7": 8,
    "6": 7,
    "5": 6,
    "4": 5,
    "3": 4,
    "2": 3,
    "J": 2,
}


def get_kind_part1(hand):
    card_count = Counter(hand)
    # print(card_count)
    # 5 of a kind
    if 5 in card_count.values():
        return 6
    # 4 of a kind
    elif 4 in card_count.values():
        return 5
    # full house
    elif 3 in card_count.values() and 2 in card_count.values():
        return 4
    # 3 of a kind
    elif 3 in card_count.values():
        return 3
    # 2 pair
    elif list(card_count.values()).count(2) == 2:
        return 2
    # one pair
    elif 2 in card_count.values():
        return 1
    # High Card
    else:
        return 0


def get_kind_part2(hand):
    card_count = Counter(hand)
    j_count = card_count.get('J', 0)
    # 5 of a kind
    if 5 in card_count.values():
        return 6
    # 4 of a kind
    elif 4 in card_count.values():
        if j_count:
            return 6
        return 5
    # full house
    elif 3 in card_count.values() and 2 in card_count.values():
        if j_count:
            return 6
        return 4
    # 3 of a kind
    elif 3 in card_count.values():
        if j_count:
            return 5
        return 3
    # 2 pair
    elif list(card_count.values()).count(2) == 2:
        if j_count == 2:
            return 5
        elif j_count == 1:
            return 4
        return 2
    # one pair
    elif 2 in card_count.values():
        if j_count:
            return 3
        return 1
    # High Card
    else:
        if j_count:
            return 1
        return 0


def compare_hands(hand1, hand2):
    hand1 = hand1[0]
    hand2 = hand2[0]
    # print(hand1, hand2)
    for i in range(5):
        if card_ranks[hand1[i]] > card_ranks[hand2[i]]:
            return 1
        elif card_ranks[hand1[i]] < card_ranks[hand2[i]]:
            return -1
    return 0


def part1(hands):
    ranks = {i: [] for i in range(7)}
    for line in hands:
        h, _ = line.split()
        bid = int(_)
        ranks[get_kind_part1(h)].append((h, bid))

    for i in range(7):
        ranks[i] = sorted(ranks[i], key=cmp_to_key(compare_hands), reverse=True)
    # print(ranks)

    count = len(hands)
    ans = 0
    for i in range(6, -1, -1):
        if len(ranks[i]) > 0:
            for j in ranks[i]:
                ans += j[1] * count
                count -= 1
    # print(ans)
    return ans


def part2(hands):
    ranks = {i: [] for i in range(7)}
    for line in hands:
        h, _ = line.split()
        bid = int(_)
        ranks[get_kind_part2(h)].append((h, bid))

    for i in range(7):
        ranks[i] = sorted(ranks[i], key=cmp_to_key(compare_hands), reverse=True)
    # print(ranks)

    count = len(hands)
    ans = 0
    for i in range(6, -1, -1):
        if len(ranks[i]) > 0:
            for j in ranks[i]:
                ans += j[1] * count
                count -= 1
    # print(ans)
    return ans


# print(part1(lines))
print(part2(lines))
