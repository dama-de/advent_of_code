import itertools, re

lines = [list(map(int, l)) for l in re.findall("(\\d+),(\\d+) -> (\\d+),(\\d+)", open("input.txt").read())]
size = max([p for p in itertools.chain(*lines)]) + 1
map = [[0] * size for i in range(size)]

sign = lambda x: -1 if x < 0 else (1 if x > 0 else 0)

for l in lines[:]:
    if not (l[0] == l[2] or l[1] == l[3]):
        continue

    lines.remove(l)

    for x in range(min(l[0], l[2]), max(l[0], l[2]) + 1):
        for y in range(min(l[1], l[3]), max(l[1], l[3]) + 1):
            map[y][x] += 1

# [print(l) for l in map]
print(len(list(filter(lambda n: n > 1, itertools.chain(*map)))))
for l in lines:
    x, y = (l[0], l[1])
    xi = sign(l[2] - l[0])
    yi = sign(l[3] - l[1])
    while x != l[2] + xi:
        map[y][x] += 1
        x += xi
        y += yi

# [print(l) for l in map]
print(len(list(filter(lambda n: n > 1, itertools.chain(*map)))))
