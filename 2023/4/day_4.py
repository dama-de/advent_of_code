f, a = open("input.txt").readlines(), 0
b = [1] * len(f)
for i, l in enumerate(f):
    w, m = l.split(":")[1].split("|")
    j, s = i + 1, len([h for h in w.split() if h in m.split()])
    a += 2 ** (s - 1) if s else 0
    b[j:j + s] = [b[j + o] + b[i] for o in range(s)]
print(a, sum(b))
