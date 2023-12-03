import re
f, a, b = open("input.txt").readlines(), 0, 0
for i, l in enumerate(f):
    y = sorted([0, len(f), i - 1, i + 2])
    for n in list(re.finditer("\\d+", l)):
        x = sorted([0, len(l), n.start() - 1, n.end() + 1])
        a += int(n[0]) * bool(re.search("[^0-9.\n]", "".join([o[x[1]:x[2]] for o in f[y[1]:y[2]]])))
    for n in list(re.finditer("\\*", l)):
        b += q[0] * q[1] if len(q := [int(p[0]) for o in f[y[1]:y[2]] for p in re.finditer("\\d+", o) if n.start() <= p.end() and n.end() >= p.start()]) == 2 else 0
print(a, b)
