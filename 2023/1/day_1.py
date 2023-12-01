d = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
f = open("input.txt").readlines()

def a(w: str):
    if not w:
        return []
    n = a(w[1::])
    return [int(w[0])] + n if w[0].isdigit() else n

def b(w: str):
    if not w:
        return []
    n = b(w[1::])
    if r := a(w[0]):
        return r + n
    for i, z in enumerate(d):
        if w.startswith(z):
            return [i+1] + n
    return n

r = lambda p: sum([10 * l[0] + l[-1] for l in p])

j, k = zip(*[[a(l), b(l)] for l in f])
print(r(j), r(k))
