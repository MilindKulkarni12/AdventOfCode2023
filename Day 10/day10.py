with open('./ex.txt', 'r') as r:
    data = [[p for p in l.strip()] for l in r.readlines()]

tiles = {
    ('|', 'bottom', '-', 'right'): 'F',
    ('|', 'bottom', '-', 'left'): '7',
    ('|', 'top', '-', 'right'): 'L',
    ('|', 'top', '-', 'left'): 'J',
    ('|', 'bottom', '-', 'right'): 'F',
    ('|', 'bottom', '-', 'left'): '7',
    ('|', 'top', '-', 'right'): 'L',
    ('|', 'top', '-', 'left'): 'J',
    ('|', 'bottom', '-', 'right'): 'F',
    ('|', 'bottom', '-', 'left'): '7',
    ('|', 'top', '-', 'right'): 'L',
    ('|', 'top', '-', 'left'): 'J',
    ('|', 'bottom', '-', 'right'): 'F',
    ('|', 'bottom', '-', 'left'): '7',
    ('|', 'top', '-', 'right'): 'L',
    ('|', 'top', '-', 'left'): 'J',
    ('|', 'bottom', '-', 'right'): 'F',
    ('|', 'bottom', '-', 'left'): '7',
    ('|', 'top', '-', 'right'): 'L',
    ('|', 'top', '-', 'left'): 'J',
}

mappings = {
    'top': '|F7',
    'bottom': '|LJ',
    'left': '-LF',
    'right': '-J7'
}


def part1(pipes):
    for i in range(len(pipes)):
        for j in range(len(pipes[i])):
            if pipes[i][j] == 'S':
                # check top:


