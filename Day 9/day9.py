with open('./input.txt', 'r') as r:
    data = [l.strip() for l in r.readlines()]


def get_difference(sequence):
    return [sequence[i+1] - sequence[i] for i in range(len(sequence)-1)]


def all_same(sequence):
    key = sequence[0]
    for i in sequence:
        if i != key:
            return False
    return True


def get_prediction(sequence):
    return sequence[0] if all_same(sequence) else sequence[-1] + get_prediction(get_difference(sequence))


def part1(sequences):
    ans = 0
    for _ in sequences:
        sequence = list(map(int, _.split()))
        ans += get_prediction(sequence)
    return ans


def part2(sequences):
    ans = 0
    for _ in sequences:
        sequence = list(map(int, _.split()))
        ans += get_prediction(sequence[::-1])
    return ans


print(part1(data))
# 1696140818
print(part2(data))
