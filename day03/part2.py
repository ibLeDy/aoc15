with open('input.txt', 'r') as f:
    moves = f.read()

sx = sy = 0
rx = ry = 0
grid = {(0, 0): 2}
directions = {'^': (0, 1),
              'v': (0, -1),
              '>': (1, 0),
              '<': (-1, 0)}


def compute_location(x, y):
    location = (x, y)
    if location not in grid:
        grid[location] = 1
    else:
        grid[location] += 1


for i, move in enumerate(moves):
    if i % 2 == 0:
        sx += directions[move][0]
        sy += directions[move][1]
        compute_location(sx, sy)
    else:
        rx += directions[move][0]
        ry += directions[move][1]
        compute_location(rx, ry)

print(len(grid.values()))
