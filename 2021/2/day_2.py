cmds = [l.strip().split(" ") for l in open("input.txt")]
x1, y1, x2, y2, a = (0, 0, 0, 0, 0)
f = {"forward": lambda n: (x1 + n, y1, x2 + n, y2 + a * n, a),
     "down": lambda n: (x1, y1 + n, x2, y2, a + n),
     "up": lambda n: (x1, y1 - n, x2, y2, a - n)}
for c in cmds:
    x1, y1, x2, y2, a = f[c[0]](int(c[1]))
print(x1 * y1, x2 * y2)
