from math import floor, ceil


def bisect(rng, lh_char, input):
    for c in input:
        newborder = rng[0] + (rng[1] - rng[0]) / 2
        rng = (rng[0], floor(newborder)) if c == lh_char else (ceil(newborder), rng[1])
    return rng[0]


if __name__ == '__main__':
    fin = open("input.txt", "r")
    lines = fin.read().split("\n")

    ids = [bisect((0, 127), "F", line[0:7]) * 8 + bisect((0, 8), "L", line[7:]) for line in lines if line]
    print(max(ids))

    for id in sorted(ids):
        if id + 1 not in ids:
            print(id + 1)
            break
