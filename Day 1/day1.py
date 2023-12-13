with open('./input.txt', 'r') as r:
    data = r.readlines()

sum = 0
for line in data:
    left, right = 0, len(line) -1
    while left < len(line):
        if line[left].isdigit():
            break
        left += 1

    while right >= 0:
        if line[right].isdigit():
            break
        right -= 1

    sum += int(''.join([line[left] + line[right]]))

print(sum)
