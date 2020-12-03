from itertools import combinations
from math import prod


def solve(filename, r):
    fin = open(filename, "r")
    lines = fin.readlines()

    nums = [int(line) for line in lines]

    for comb in combinations(nums, r):
        if sum(comb) == 2020:
            print(comb)
            print(prod(comb))


if __name__ == '__main__':
    solve("input.txt", 2)
    solve("input.txt", 3)
