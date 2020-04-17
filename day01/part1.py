with open('input.txt', 'r') as fp:
    instructions = [i for i in fp.read()]

floor = 0
for move in instructions:
    if move == '(':
        floor += 1
    elif move == ')':
        floor -= 1

print(floor)
