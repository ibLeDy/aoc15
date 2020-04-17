with open('input.txt', 'r') as f:
    moves = f.read()

x = y = 0
grid = {(x, y): 1}
directions = {'^': (0, 1),
              'v': (0, -1),
              '>': (1, 0),
              '<': (-1, 0)}

for move in moves:
    x += directions[move][0]
    y += directions[move][1]

    location = (x, y)
    if location not in grid:
        grid[location] = 1
    else:
        grid[location] += 1

print(len(grid.values()))
