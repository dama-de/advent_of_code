lz = lambda l: list(zip(*l))
lf = lambda l, i, b: list(filter(lambda n: n[i] == b, l))
s = lambda n: "0" if n.count("0") > n.count("1") else "1"
f = open("input.txt").read().splitlines()
z = lz(f)
g = e = ""
o = c = f.copy()
for i in range(len(z)):
    g += s(z[i])
    e += "0" if g[-1] == "1" else "1"
    if len(o) > 1:
        m = s(lz(o)[i])
        o = lf(o, i, m)
    if len(c) > 1:
        l = "1" if s(lz(c)[i]) == "0" else "0"
        c = lf(c, i, l)
print(int(g, 2) * int(e, 2), int(o[0], 2) * int(c[0], 2))
