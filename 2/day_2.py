import re


def solve(lines):
    one, two = 0, 0

    for line in lines:
        match = re.match("(\\d+)-(\\d+) (\\w): (\\w+)", line)
        omin, omax, char, word = match.groups()

        if int(omin) <= word.count(char) <= int(omax):
            one = one + 1

        if (word[-1 + int(omin)] == char) ^ (word[-1 + int(omax)] == char):
            two = two + 1

    print(one)
    print(two)


if __name__ == '__main__':
    fin = open("input.txt", "r")
    lines = fin.readlines()

    solve(lines)
