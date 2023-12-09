SPECIAL_CHARS = ['@', '#', '$', '%', '&', '*', '+', '-', '/', '=']

with open('./input.txt', 'r') as r:
    data = r.readlines()

matrix = []
for line in data:
    matrix.append(line)


def fetch_number(i, j, n, matrix):
    while j > 0 and matrix[i][j-1].isdigit():
        j -= 1
    num = ''
    while j < n and matrix[i][j].isdigit():
        num += matrix[i][j]
        j += 1
    return i, j, int(num)


def map_sym_to_num(i, j, sym_to_num):
    sym_key = f'{i}_{j}'
    if sym_key in sym_to_num:
        sym_to_num[sym_key].append(num)
    else:
        sym_to_num[sym_key] = [num]


n = len(matrix)
found_num = {}
sym_to_num = {}
part_numbers = []

for i in range(n):
    for j in range(n):
        if matrix[i][j] in SPECIAL_CHARS:
            # left
            if j > 0 and matrix[i][j-1].isdigit():
                idash, jdash, num = fetch_number(i, j-1, n, matrix)
                key = f'{idash}{jdash}_{num}'
                if key not in found_num:
                    part_numbers.append(num)
                    found_num[key] = True
                    map_sym_to_num(i, j, sym_to_num)
            # right
            if j < n-1 and matrix[i][j+1].isdigit():
                idash, jdash, num = fetch_number(i, j+1, n, matrix)
                key = f'{idash}{jdash}_{num}'
                if key not in found_num:
                    part_numbers.append(num)
                    found_num[key] = True
                    map_sym_to_num(i, j, sym_to_num)
            # top
            if i > 0 and matrix[i-1][j].isdigit():
                idash, jdash, num = fetch_number(i-1, j, n, matrix)
                key = f'{idash}{jdash}_{num}'
                if key not in found_num:
                    part_numbers.append(num)
                    found_num[key] = True
                    map_sym_to_num(i, j, sym_to_num)
            # top left
            if i > 0 and j > 0 and matrix[i-1][j-1].isdigit():
                idash, jdash, num = fetch_number(i-1, j-1, n, matrix)
                key = f'{idash}{jdash}_{num}'
                if key not in found_num:
                    part_numbers.append(num)
                    found_num[key] = True
                    map_sym_to_num(i, j, sym_to_num)
            # top right
            if i > 0 and j < n-1 and matrix[i-1][j+1].isdigit():
                idash, jdash, num = fetch_number(i-1, j+1, n, matrix)
                key = f'{idash}{jdash}_{num}'
                if key not in found_num:
                    part_numbers.append(num)
                    found_num[key] = True
                    map_sym_to_num(i, j, sym_to_num)
            # bottom
            if i < n-1 and matrix[i+1][j].isdigit():
                idash, jdash, num = fetch_number(i+1, j, n, matrix)
                key = f'{idash}{jdash}_{num}'
                if key not in found_num:
                    part_numbers.append(num)
                    found_num[key] = True
                    map_sym_to_num(i, j, sym_to_num)
            # bottom left
            if i < n-1 and j > 0 and matrix[i+1][j-1].isdigit():
                idash, jdash, num = fetch_number(i+1, j-1, n, matrix)
                key = f'{idash}{jdash}_{num}'
                if key not in found_num:
                    part_numbers.append(num)
                    found_num[key] = True
                    map_sym_to_num(i, j, sym_to_num)
            # bottom right
            if i < n-1 and j < n-1 and matrix[i+1][j+1].isdigit():
                idash, jdash, num = fetch_number(i+1, j+1, n, matrix)
                key = f'{idash}{jdash}_{num}'
                if key not in found_num:
                    part_numbers.append(num)
                    found_num[key] = True
                    map_sym_to_num(i, j, sym_to_num)

# print(sum(part_numbers))
total_ratio = 0
for sym, mappings in sym_to_num.items():
    if len(mappings) == 2:
        total_ratio += mappings[0]*mappings[1]
print(total_ratio)
