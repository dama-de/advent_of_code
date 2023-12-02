import re
f, x, y = open("input.txt"), 0, 0
for i, l in enumerate(f):
    r, g, b = [max([int(n) for n in m]) for c in ['r', 'g', 'b'] if (m := re.findall(f"(\\d+) {c}", l))]
    x += (i+1) * all([r < 13, g < 14, b < 15])
    y += r * g * b
print(x, y)
