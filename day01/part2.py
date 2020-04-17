with open('input.txt', 'r') as fp:
    instructions = [i for i in fp.read()]

floor = 0
basement_idx = -1
for idx, move in enumerate(instructions):
    if move == '(':
        floor += 1
    elif move == ')':
        floor -= 1

    if abs(floor) != floor and basement_idx == -1:
        basement_idx = idx + 1

print(basement_idx)
