def solve(lines, slope_x, slope_y=1):
    trees, x = 0, 0
    for y in range(0, len(lines), slope_y):
        line = lines[y][:-1]
        if line[x] == '#':
            trees = trees + 1
        x = (x + slope_x) % len(line)
    return trees


if __name__ == '__main__':
    fin = open("input.txt", "r")
    lines = fin.readlines()

    print(solve(lines, 3))

    print(solve(lines, 1)
          * solve(lines, 3)
          * solve(lines, 5)
          * solve(lines, 7)
          * solve(lines, 1, 2))
