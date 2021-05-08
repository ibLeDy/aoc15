with open('input.txt', 'r') as fp:
    dimensions = [tuple(map(int, line.strip().split('x'))) for line in fp.readlines()]

total_feet = 0
for l, w, h in dimensions:  # noqa: E741
    wrapping_paper = (2 * l * w) + (2 * w * h) + (2 * h * l)
    wrapping_paper += min([l * w, w * h, h * l])
    total_feet += wrapping_paper

print(total_feet)
