with open('input.txt', 'r') as fp:
    dimensions = [tuple(map(int, line.strip().split('x'))) for line in fp.readlines()]

total_feet = 0
for l, w, h in dimensions:
    sides = sorted([l, w, h])
    ribbon = (2 * sides[0]) + (2 * sides[1])
    ribbon += l * w * h
    total_feet += ribbon

print(total_feet)
