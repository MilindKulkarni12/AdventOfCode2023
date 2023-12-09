COLOUR_COUNT = {
    'red': 12,
    'green': 13,
    'blue': 14
}

with open('./input.txt', 'r') as r:
    data = r.readlines()


def part1(lines):
    valid_games = []
    for line in lines:
        game_tag, all_games = line.split(':', 1)
        game_num = int(game_tag.split()[1])
        invalid = False

        for sub_games in all_games.split(';'):
            sub_games = sub_games.split(',')
            for game in sub_games:
                count, colour = game.split()
                count = int(count)

                if count > COLOUR_COUNT[colour]:
                    invalid = True

        if not invalid:
            valid_games.append(game_num)
    return sum(valid_games)


def part2(lines):
    cross_products = []
    for line in lines:
        max_colour = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        game_tag, all_games = line.split(':', 1)

        for sub_games in all_games.split(';'):
            sub_games = sub_games.split(',')
            for game in sub_games:
                count, colour = game.split()
                count = int(count)

                if count > max_colour[colour]:
                    max_colour[colour] = count

        cross_products.append(max_colour['red'] * max_colour['green'] * max_colour['blue'])

    return sum(cross_products)


# print(part1(data))
print(part2(data))
