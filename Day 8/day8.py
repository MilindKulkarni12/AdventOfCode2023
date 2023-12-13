import math


def read_file(file_name):
    input_array = []
    with open(file_name, "r") as file:
        for line in file:
            input_array.append(line.strip())
        return input_array


lines = read_file("input.txt")

rules = lines[0]
chooseRL = {
    'L': 0,
    'R': 1,
}
data = {}

for i in range(2, len(lines)):
    src, dst = lines[i].split("=")
    data[src.strip()] = list(i.strip() for i in dst.strip("( )").split(","))


def part1(rules, directions, chooseRL, curr='AAA'):
    i, count = 0, 0
    while curr[-1] != 'Z':
        rl = rules[i]
        idx = chooseRL[rl]
        curr = directions[curr][idx]
        i = (i + 1) % len(rules)
        count += 1

    return count


def part2(rules, directions, chooseRL):
    curr_nodes = {k: 0 for k in directions.keys() if k[-1] == 'A'}
    for k in curr_nodes.keys():
        curr_nodes[k] = part1(rules, directions, chooseRL, k)
    print(curr_nodes)
    return list(curr_nodes.values())


# part1(rules, data, chooseRL)
ans = part2(rules, data, chooseRL)
print(math.lcm(*ans))
